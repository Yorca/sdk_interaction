

import json

with open("data/api_summary_groundtruth.json", "r") as file:
    data = file.read()

data = json.loads(data)["LIBS"]

apis = []
for item in data:
    for api in item["privacy_APIs"]:
        apis.append({
            "method_name" : api["API_name"],
            "class_name": api["class_name"],
            "conditions": api["conditions"],
            "effects": api["effects"]
        })


with open("pure_api_list.json", "a") as file:
    file.write(str(apis))