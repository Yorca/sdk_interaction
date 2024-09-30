

with open("downloaded_pkg.txt", "r") as file:
    downloads = file.readlines()
    downloads = [download.replace("\n", "") for download in downloads]

import pandas as pd

total_data = pd.read_csv("app_metadata_topfree_merged.csv")

for index, row in total_data.iterrows():
    if row[0] not in downloads:
        with open("download_tasls.txt", "a") as file:
            file.write(f"{row[0]}\n")


            