import os.path

from google_play_scraper import app
import pandas as pd
import json

pkg_data = pd.read_csv("../apk_downloader/app_metadata_topfree_merged.csv")
details_path = "app_details"
for _, row in pkg_data.iterrows():
    pkg_name = row[0]
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