import re
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from tqdm import tqdm
import requests
import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd
import traceback
from datetime import datetime

# code ref: https://github.com/anishomsy/apkpure

server_path = "/Users/yorca/projects/sdk_interaction/py/apk_downloader/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
}

last_download_time = datetime.now()
execute_apk_list = []
apk_path = f"{server_path}apks_new"
if not os.path.exists(apk_path):
    os.makedirs(apk_path)

if os.path.exists(f"{server_path}downloaded_pkg.txt"):
    with open(f"{server_path}downloaded_pkg.txt", "a") as file:
        file.write("")
with open(os.path.join(server_path, f"{server_path}downloaded_pkg.txt"), "r") as file:
    execute_apk_list = file.readlines()
execute_apk_list = [apk.replace("\n", "") for apk in execute_apk_list]

for filename in os.listdir(apk_path):
    execute_apk_list.append(filename.split('---')[0])

def log_error(TAG, info):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    with open(f"{server_path}download.log", "a") as file:
        file.write(f"---------------------------------{formatted_time}\nTAG: {TAG}, error: {info}\n")
    print(f"ERROR - TAG: {TAG}  info: {info}")

def get_response(url: str, **kwargs) -> requests.Response | None:
    response = requests.get(url, headers)

    if response.status_code == 403:
        scraper = cloudscraper.create_scraper()
        response = scraper.get(url=url, **kwargs)

    # Return the response if the response is successful i.e status_code == 200
    return response if response.status_code == 200 else None


def extract_apk_info_from_url(url):
    response = get_response(url)
    if response == None:
        log_error("Empty Response", url)
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all elements under 'download-btn-box' and extract 'data-dt-version_code' and 'data-dt-apkid'
    download_btn_box = soup.find_all('div', {'class': 'download-btn-box'})
    result = []

    for box in download_btn_box:
        apk_link = box.find('a', class_='download_apk_news')
        version_code = apk_link.get('data-dt-version_code')
        apkid = apk_link.get('data-dt-apkid')
        apkid_data = apkid.split('/')
        apk_type = None
        if len(apkid_data) >= 2 and apkid_data[1].lower() in ['apk', 'xapk']:
            apk_type = apkid_data[1]

        result.append({
            'version_code': version_code,
            'apk_type': apk_type
       })

    return result[0]


def download_apk(package_name, apk_type):
    url = f"https://d.apkpure.com/b/{apk_type}/{package_name}?version=latest"
    print(f"url = {url}")
    response = get_response(
        url=url, stream=True, allow_redirects=True, headers=headers
    )
    if response == None:
        raise Exception("Get Empty Response")
    d = response.headers.get("content-disposition")
    if d == None:
        raise Exception("content-disposition failed")
    # fname = f".{apk_type.lower()}"
    fname = re.findall("filename=(.+)", d)[0].strip('"')


    fname = os.path.join(os.getcwd(), f"{apk_path}/{package_name}---{fname}")

    os.makedirs(os.path.dirname(fname), exist_ok=True)
    if os.path.exists(fname) and int(
            response.headers.get("content-length", 0)
    ) == os.path.getsize(fname):
        print("File Exists!")
        return os.path.realpath(fname)

    with tqdm.wrapattr(
            open(fname, "wb"),
            "write",
            miniters=1,
            total=int(response.headers.get("content-length", 0)),
    ) as file:
        for chunk in response.iter_content(chunk_size=4 * 1024):
            if chunk:
                file.write(chunk)

    execute_apk_list.append(package_name)
    with open(f"{server_path}downloaded_pkg.txt", "a") as file:
        file.write(f"{package_name}\n")
    global last_download_time
    last_download_time = datetime.now()
    return os.path.realpath(fname)


def process_apk(apk):
    try:
        download_apk(apk, "APK")
    except Exception as e:
        try:
            log_error("Download Failed", f"{apk}: {str(e)}")
            download_apk(apk, "XAPK")
        except Exception as e:
            log_error("Download Failed", f"{apk}: {str(e)}")

with open(f"{server_path}download_tasks.txt", "r") as file:
    apk_list = file.readlines()
    apk_list = [apk.replace("\n", "") for apk in apk_list]

for apk in apk_list[2500:3500]:
    if apk in execute_apk_list:
        print(f"has download: {apk}")
        continue
    current_time = datetime.now()
    time_difference = current_time - last_download_time
    minutes_difference = time_difference.total_seconds() / 60
    if minutes_difference > 10:
        log_error("Exceed max failed time", "no download over 10 minutes, stop, wait next timed task")
        break
    process_apk(apk)