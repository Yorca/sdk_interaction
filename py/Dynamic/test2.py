import json
import os

apis = []
for filename in os.listdir("../DocAndSummary/Doc/GPT Summarizer/summary/sum9"):
    path = os.path.join("../DocAndSummary/Doc/GPT Summarizer/summary/sum9", filename)
    with open(path, "r") as file:
        data = json.load((file))

    sdk = data['SDK']
    for api in data["privacy_APIs"]:
        apis.append(f"{sdk};{api['API_name']}")

apis = list(set(apis))
print(len(apis))
apis_gt = []
with open("data/api_summary_groundtruth.json", "r") as file:
    data = json.load(file)
for lib in data["LIBS"]:
    sdk = lib["SDK"]
    for api in lib["privacy_APIs"]:
        apis_gt.append(f"{sdk};{api['API_name']}")
apis_gt = list(set(apis_gt))

count = 0
for api in apis_gt:
    if api in apis:
        count += 1
print(f"{count}/{len(apis_gt)}")