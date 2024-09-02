import os
import time

import requests
import pandas as pd

def save_webpage(url, name):

    # Fetch the webpage content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the content to a file
        with open(f"website_sup/{name}.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        time.sleep(3)
    else:
        with open(f"archive_log_sup.txt", "w", encoding="utf-8") as file:
            file.write(f"Failed to fetch the webpage. url: {url} name:{name}")



df = pd.read_excel('doc_dataset2.0.xlsx')

def archive_docs(sdk, docs, tag):
    for i, item in enumerate(docs):
        if not item or item.strip() == 'nan' or item.strip() == '':
            continue
        title = f"{sdk}_{tag}{'' if i == 0 else i}"
        save_webpage(item, title)

for index, row in df.iterrows():
    sdk_name = row[0]
    has_pri_api = row[2]
    is_sup = row[1] == "Supplement"
    if not has_pri_api or not is_sup:
        continue
    print(sdk_name)
    integ_docs = str(row[6]).split(';')
    priv_docs = str(row[7]).split(';')
    medi_docs = str(row[8]).split(';')
    archive_docs(sdk_name, integ_docs, "integration")
    archive_docs(sdk_name, priv_docs, "privacy")
    archive_docs(sdk_name, medi_docs, "mediation")