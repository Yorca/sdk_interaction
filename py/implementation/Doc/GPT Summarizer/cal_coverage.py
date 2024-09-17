import json

import pandas
import pandas as pd
import os
gt_data = pd.read_excel('data/API_GT.xlsx')

sdks = os.listdir("../web_archive/privacy_doc_md_final/")

res_data = pd.read_excel("data/Updated_Summary_Evaluationmd_merge.xlsx")

gt_apis = []
res_apis = []
link = {}
for index, row in gt_data.iterrows():
    apis = row[2].split(',')
    apis = [api.strip() for api in apis]
    gt_apis += [f"{row[0]};{api}" for api in apis]
    link[row[0]] = row[1]


for index, row in res_data.iterrows():
    if isinstance(row[2], str) and not row[2] == "nan":
        apis = row[2].split(',')
        apis = [api.strip() for api in apis]
        res_apis += [f"{row[0]};{api}" for api in apis]

count = 0
for api in gt_apis:
    if api in res_apis:
        count += 1
print(f"{count}/{len(gt_apis)} = {count/(len(gt_apis))}")


for index, row in gt_data.iterrows():
    for index2, row2 in res_data.iterrows():
        if row2[0] == row[0]:
            gt_data.at[index, 3] = row2[2]


# gt_data.to_excel("data/merger_res.xlsx")
df = pandas.DataFrame(columns=["SDK", "API", "Summary","links"])
# get summary set
for item in gt_apis:
    [sdk, api] = item.split(';')

    print(sdk)
    with open(f"summary/merged/{sdk}.json", "r") as file:
        data = file.read()
    js = json.loads(data)
    has_sum = False
    for sum in js["privacy_APIs"]:
        if sum["API_name"] == api:
            df.loc[len(df)] = [sdk, api, sum, link[sdk]]
            has_sum = True
            break
    if not has_sum:
        df.loc[len(df)] = [sdk, api, "null", link[sdk]]
df.to_excel("data/summary_set_merged.xlsx", index=False)
