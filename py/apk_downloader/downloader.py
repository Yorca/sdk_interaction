import re
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import shutil
from tqdm import tqdm
import requests
import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd
import traceback
from datetime import datetime

# code ref: https://github.com/anishomsy/apkpure
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
}

last_download_time = datetime.now()
execute_apk_list = []
apk_path = "/Volumes/T7 Shield/success_redownload" #  f"{server_path}apks_new"
if not os.path.exists(apk_path):
    os.makedirs(apk_path)

with open(f"downloaded_pkg.txt", "a") as file:
    file.write("")

with open("downloaded_pkg.txt", "r") as file:
    execute_apk_list = file.readlines()
execute_apk_list = [apk.replace("\n", "") for apk in execute_apk_list]

for filename in os.listdir(apk_path):
    execute_apk_list.append(filename.split('---')[0])

def remove_failded_pkg(apk):
    for filename in os.listdir(apk_path):
        if filename.startswith(f"{apk}---"):
            file_path = os.path.join(apk_path, filename)
            os.remove(file_path)

def log_error(TAG, info):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    with open(f"download.log", "a") as file:
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

    # apk priority
    for item in result:
        if item["apk_type"].lower() == "apk":
            return item

    return result[0]


def download_apk(package_name, version_code,apk_type):
    url = f"https://d.apkpure.com/b/{apk_type}/{package_name}?versionCode={version_code}"
    print(f"url = {url}")
    response = get_response(
        url=url, stream=True, allow_redirects=True, headers=headers
    )
    if response == None:
        raise Exception("Get Empty Response")
    d = response.headers.get("content-disposition")
    if d == None:
        raise Exception("content-disposition failed")

    base_name = f"{package_name}.{apk_type.lower()}"
    fname = os.path.join(os.getcwd(), f"{apk_path}/{base_name}")

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
    global last_download_time
    last_download_time = datetime.now()
    execute_apk_list.append(package_name)
    with open("downloaded_pkg.txt", "a") as file:
        file.write(f"{package_name}\n")
    # try:
    #     sftp.put(fname, f"{server_dir}/{base_name}")
    #     os.remove(fname)
    # except:
    #     log_error("upload_failed", package_name)

    # with open(upload_record, "a") as file:
    #     file.write(f"{package_name}\n")

    return os.path.realpath(fname)


def process_apk(apk):
    try:
        apk_info = extract_apk_info_from_url(f"https://apkpure.com/apk/{apk}")
        version_code = apk_info["version_code"]
        apk_type = apk_info["apk_type"]

        if version_code is None:
            log_error(apk, "empty version code")
            return
        if apk_type is None:
            log_error(apk, "empty apk type")
            apk_type = 'APK'  # use APK to try

        download_apk(apk, version_code, apk_type)
    except Exception as e:
        error_message = str(e)
        stack_trace = traceback.format_exc()
        log_error(apk, f"{error_message}\nStack trace:\n{stack_trace}")

with open("../../google play scraper/data/app_metadata_topfree-100.csv", "r") as file:
    lines = file.readlines()
lines = [line.split('","')[0].replace('"','') for line in lines[1:] if not line == '']

apk_list = list(set(lines))
apk_list.remove('')

with open("../apps/install/success.txt", "r") as file:
    success_apks = file.readlines()
success_apks = [apk.replace(".apk\n", "") for apk in success_apks]
count = 0
for apk in apk_list:
    if apk in success_apks:
        count += 1

apk_list = list(set(apk_list))

with ThreadPoolExecutor(max_workers=10000) as executor:
    futures = []
    for apk in success_apks:
        # if apk in success_apks:
        #     continue
        if apk in execute_apk_list:
            print(f"has download: {apk}")
            continue

        current_time = datetime.now()

        time_difference = current_time - last_download_time
        minutes_difference = time_difference.total_seconds() / 60
        if minutes_difference > 10:
            log_error("Exceed max failed time", "no download over 10 minutes, stop, wait next timed task")
            break
        futures.append(executor.submit(process_apk, apk))
        time.sleep(3)

    for future in as_completed(futures):
        future.result()
