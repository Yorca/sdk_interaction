import json
import os

import pandas as pd

data = pd.read_excel("/Users/yorca/projects/sdk_interaction/py/implementation/Doc/GPT Summarizer/data/API_GT.xlsx")

api_gt = []

for index, row in data.iterrows():
    apis = row[2].split(",")
    apis = [api.strip() for api in apis]
    api_gt += apis

print(api_gt)

count = 0
for api in api_gt:
    file = f"res/{api}.json"
    if not os.path.exists(file):
        continue
    with open(f"res/{api}.json", "r") as file:
        api_data = file.read()
        js_data = json.loads(api_data)
        if len(js_data.keys()) > 0:
            count +=1
print(f"{count}/{len(api_gt)}")