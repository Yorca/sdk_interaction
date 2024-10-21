import os

with open("downloaded_pkg3.txt", "r") as file:
    downloads = file.readlines()
    downloads = [download.replace("\n", "") for download in downloads]

import pandas as pd

total_data = pd.read_csv("app_metadata_topfree_merged.csv")
all_pkgs = []
for index, row in total_data.iterrows():
    all_pkgs.append(row[0])
    # if row[0] not in downloads:
    #     with open("download_tasks.txt", "a") as file:
    #         file.write(f"{row[0]}\n")

all_pkgs = list(set(all_pkgs))
print(len(all_pkgs))

# pkgs2 = []
# for download in downloads:
#     if download not in all_pkgs and download.split('_')[0] in all_pkgs:
#         pkg = download.split('_')[0]
#         pkgs2.append(pkg)
#         # if pkg in downloads or pkg in pkgs:
#         #     print(pkg)
# for pkg in all_pkgs:
#     if pkg not in downloads and pkg not in pkgs and pkg not in pkgs2:
#         with open("download_tasks.txt", "a") as file:
#             file.write(f"{pkg}\n")

# pkgs3 = []
# for download in downloads:
#      if download not in all_pkgs and download.split('_')[0] in all_pkgs:
#          pkgs3.append(download.split('_')[0])
#
# count = 0
# for pkg3 in pkgs3:
#     if pkg3 in pkgs:
#         count += 1
#         print(pkg3)
#
# print(count)