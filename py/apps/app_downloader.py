import re
import os
import time

from tqdm import tqdm
import requests
import cloudscraper
from bs4 import BeautifulSoup

# code ref: https://github.com/anishomsy/apkpure

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
}

def get_response(url: str, **kwargs) -> requests.Response | None:
    response = requests.get(url, headers)

    if response.status_code == 403:
        scraper = cloudscraper.create_scraper()
        response = scraper.get(url=url, **kwargs)

    # Return the response if the response is successful i.e status_code == 200
    return response if response.status_code == 200 else None

def extract_apk_info_from_url(url):
    response = get_response(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all elements under 'download-btn-box' and extract 'data-dt-version_code' and 'data-dt-apkid'
    download_btn_box = soup.find_all('div', {'class': 'download-btn-box'})
    print(download_btn_box)
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

def download_apk(package_name, version_code, apk_type):
    url = f"https://d.apkpure.com/b/{apk_type}/{package_name}?versionCode={version_code}"

    response = get_response(
        url=url, stream=True, allow_redirects=True, headers=headers
    )

    d = response.headers.get("content-disposition")
    fname = re.findall("filename=(.+)", d)[0].strip('"')

    fname = os.path.join(os.getcwd(), f"apks/{fname}")

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

    return os.path.realpath(fname)

def log_error(apk, info):
    with open("download.log", "a") as file:
        file.write(f"APK: {apk}, error: {info}")

apk_list = ["com.stuzo.chevron", "com.facebook.katana"]
for apk in apk_list:
    time.sleep(5)
    apk_info = extract_apk_info_from_url(f"https://apkpure.com/apk/{apk}")
    version_code = apk_info["version_code"]
    apk_type = apk_info["apk_type"]
    if version_code == None:
        log_error(apk, "empty version code")
        continue
    if apk_type == None:
        log_error(apk, "empty apk type")
        apk_type = "APK" # use APK to try
    try:
        download_apk(apk, version_code, apk_type)
    except Exception as e:
        log_error(apk, str(e))

