from loaders import load_web
import os.path

from google_play_scraper import app
import pandas as pd
import json

# pkg_data = pd.read_csv("../apk_downloader/data/app_metadata_topfree_merged.csv")

import os
import time

import requests
import pandas as pd
from bs4 import BeautifulSoup
def save_webpage(url, name):

    # Fetch the webpage content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the content to a file

        with open(f"data/data_safety/{apk}.html","w", encoding="utf-8") as file:
            file.write(response.text)
        return response.text

    else:
        with open(f"archive_log_sup.txt", "w", encoding="utf-8") as file:
            file.write(f"Failed to fetch the webpage. url: {url} name:{name}")
    return None


with open("../apps/data/app_metadata_topfree-100.csv", "r") as file:
    lines = file.readlines()
lines = [line.split('","')[0].replace('"','') for line in lines[1:] if not line == '']

apk_list = list(set(lines))
apk_list.remove('')
count = 0
for apk in apk_list:
    # datasafety_info = load_web(f"https://play.google.com/store/apps/datasafety?id={apk}&hl=en&gl=us")
    #
    # data = "\n".join([doc.page_content for doc in datasafety_info])
    # with open(f"data/data_safety/{apk}.log", "a") as file:
    #     file.write(data)
    # if "google play family" in data.lower():
    #     print(datasafety_info)
    text = save_webpage(f"https://play.google.com/store/apps/datasafety?id={apk}&hl=en&gl=us", apk)
    if text and "Committed to follow the Play Families Policy".lower() in text.lower():
        count += 1
        with open(f"res/laws/google_play_family.log", "a") as file:
            file.write(f"{apk}\n")
print(count)