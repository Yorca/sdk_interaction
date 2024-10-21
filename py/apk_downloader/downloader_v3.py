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
import paramiko

# code ref: https://github.com/anishomsy/apkpure

# server
hostname = 'brooks.cs.ucf.edu'
username = 'zh844971'
password = '!Qwert825215'
server_dir = '/home/zh844971/sdk_interaction/apks1'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, username=username, password=password)
sftp = ssh.open_sftp()

project_path = "/Users/yorca/projects/sdk_interaction/py/apk_downloader/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
}

last_download_time = datetime.now()
apk_path = f"{project_path}apks"

upload_record = f"{project_path}uploaded_apks.txt"
if not os.path.exists(upload_record):
    with open(upload_record, 'w') as file:
        file.write('')
with open(upload_record, "r") as file:
    execute_apk_list = file.readlines()
execute_apk_list = [apk.replace("\n", "") for apk in execute_apk_list]
print(f"execute_apk_list = {execute_apk_list}")
if not os.path.exists(apk_path):
    os.makedirs(apk_path)
# for filename in os.listdir(apk_path):
#     execute_apk_list.append(filename.split('---')[0])





def log_error(TAG, info):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    with open(f"{project_path}download.log", "a") as file:
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
    # fname = f".{apk_type.lower()}"
    fname = re.findall("filename=(.+)", d)[0].strip('"')

    base_name = f"{package_name}---{fname}"
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
    try:
        sftp.put(fname, f"{server_dir}/{base_name}")
        os.remove(fname)
    except:
        log_error("upload_failed", package_name)

    with open(upload_record, "a") as file:
        file.write(f"{package_name}\n")

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
    # try:
    #     download_apk(apk, "APK")
    # except Exception as e:
    #     try:
    #         error_message = str(e)
    #         stack_trace = traceback.format_exc()
    #         log_error(apk, f"Download Failed {error_message}\nStack trace:\n{stack_trace}")
    #         download_apk(apk, "XAPK")
    #     except Exception as e:
    #         error_message = str(e)
    #         stack_trace = traceback.format_exc()
    #         log_error(apk, f"Download Failed {error_message}\nStack trace:\n{stack_trace}")


    # try:
    #     apk_info = extract_apk_info_from_url(f"https://apkpure.com/apk/{apk}")
    #     version_code = apk_info["version_code"]
    #     apk_type = apk_info["apk_type"]
    #
    #     if version_code is None:
    #         log_error(apk, "empty version code")
    #         return
    #     if apk_type is None:
    #         log_error(apk, "empty apk type")
    #         apk_type = 'APK'  # use APK to try
    #
    #     download_apk(apk, version_code, apk_type)
    # except Exception as e:
    #     error_message = str(e)
    #     stack_trace = traceback.format_exc()
    #     log_error(apk, f"{error_message}\nStack trace:\n{stack_trace}")

apk_data = pd.read_csv(f"{project_path}app_metadata_topfree_merged.csv")
apk_list = []
for index, row in apk_data.iterrows():
    apk_list.append(row[0])


# apk_list = ["com.stuzo.chevron", "com.facebook.katana"]

for apk in apk_list[:3364]:
    if apk in execute_apk_list:
        print(f"has download: {apk}")
        continue
    current_time = datetime.now()
    time_difference = current_time - last_download_time
    minutes_difference = time_difference.total_seconds() / 60
    if minutes_difference > 8:
        log_error("Exceed max failed time", "no download over 8 minutes, stop, wait next timed task")
        sftp.close()
        ssh.close()
        break
    process_apk(apk)
sftp.close()
ssh.close()