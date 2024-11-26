import os.path

from google_play_scraper import app
import pandas as pd
import json

# pkg_data = pd.read_csv("../apk_downloader/data/app_metadata_topfree_merged.csv")

with open("../../google play scraper/data/app_metadata_topfree-100.csv", "r") as file:
    lines = file.readlines()
lines = [line.split('","')[0].replace('"','') for line in lines[1:] if not line == '']

apk_list = list(set(lines))
apk_list.remove('')
print(apk_list)
print(len(apk_list))


details_path = "app_details_5000"
for pkg_name in apk_list:
    detail_path = os.path.join(details_path, pkg_name)
    if os.path.exists(detail_path):
        continue
    try:
        detail = app(pkg_name, "en")
        detail_js = json.dumps(detail, indent=4)
        with open(detail_path, "a") as file:
            file.write(detail_js)
        print(f"Scrape {pkg_name} Success!")
    except Exception as e:
        with open("detail_scarper_error.log", "a") as file:
            file.write(f"pkg: {pkg_name}, Error: {e}\n")