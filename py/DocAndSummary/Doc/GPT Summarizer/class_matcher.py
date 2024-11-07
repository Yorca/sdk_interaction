import pandas as pd
import os


def parse_class_info(filepath):

    with open(filepath, "r") as file:
        lines = file.readlines()


    class_info = {}
    for line in lines:
        [sdk, _, method, sig] = [item.strip() for item in line.split("---")]
        if sdk in class_info and method in class_info[sdk]:
            if sig not in class_info[sdk][method]:
                class_info[sdk][method].append(sig)
        else:
            class_info.setdefault(sdk, {}).setdefault(method, []).append(sig)
    return class_info


class_matched_info = parse_class_info("data/class_match/method_class_match.txt")
class_only_info = parse_class_info("data/class_match/method_only_match.txt")

pri_gt = pd.read_excel("data/API_GT_NEW.xlsx")
apis_info = {}

for index, row in pri_gt.iterrows():
    apis = row[1].split("/")
    print(apis)
    # if "，" in row[2] or "；" in row[2] or ";" in row[2]:
    #     print(row[2])
    apis = [api.strip() for api in apis]
    if row[0] in apis_info:
        apis_info[row[0]] += apis
    else:
        apis_info[row[0]] = apis

def append_matched_class(df, class_info):
    for index, row in df.iterrows():
        sdk = row[0]
        api = row[1]
        if sdk in apis_info and api in apis_info[sdk]:
            df.at[index, 'is_privacy'] = True
        if not row[3] == None:
            continue

        if sdk in class_info and api in class_info[sdk]:
            df.at[index, 'signatures'] = class_info[sdk][api]

api_data = pd.read_csv("data/privacy_apis.csv")
api_data['signatures'] = None
api_data['is_privacy'] = False

append_matched_class(api_data, class_matched_info)
append_matched_class(api_data, class_only_info)

apis_count = 0
founded_count = 0
for index, row in api_data.iterrows():
    if row[4] == True:
        apis_count += 1
        if not row[3] == None:
            founded_count += 1

print(f"found {founded_count}/{apis_count}")
api_data.to_csv("data/api_class_match3.csv", index=False)


