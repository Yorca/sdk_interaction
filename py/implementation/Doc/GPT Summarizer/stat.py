import os

# sdk_list = []
# for dr in os.listdir("summaries2.0"):
#     sdk_list.append(dr.replace(".json", ""))
# print(sdk_list)
#
# for dr2 in os.listdir("plaintext_summaries2.0"):
#     sdk = dr2.replace(".txt", "")
#     if sdk not in sdk_list:
#         print(sdk)


import pandas as pd
import json

data = pd.read_excel("API_extraction_data.xlsx", sheet_name="API Extraction Evaluation3.0")
total_APIs = 0
found_APIs = 0
FP_count = 0
correct_found_APIs = 0
sum_df = pd.DataFrame(columns=["SDK", "API", "summary"])
sum_index = 0
for index, item in data.iterrows():
    found = item[4]
    if pd.notna(found) and not isinstance(found, str):
        found = found.strftime("%m/%d")
    correct_found_APIs += int(found.split('/')[0])
    total_APIs += int(found.split('/')[1])
    FP_count += int(item[5])
    manual_apis = item[6].split(',')
    manual_apis = [api.strip() for api in manual_apis]
    sdk = item[0]

    with open(f"summaries3.0/{sdk}.json") as file:
        sdk_summary = json.loads(file.read())
    for api in manual_apis:
        summary_text = ""
        for sum_api in sdk_summary["privacy_APIs"]:
            if sum_api["API_name"] == api:
                summary_text += str(sum_api)
        sum_df.loc[sum_index] = [sdk, api, summary_text]
        sum_index += 1


    if pd.notna(item[2]):
        found_APIs += len(item[2].split(','))

        f_apis = item[2].split(',')
        f_apis = [api.strip() for api in f_apis]
        m_apis = item[6].split(',')
        m_apis = [api.strip() for api in m_apis]
        count = 0
        for api in f_apis:
            if api in m_apis:
                count += 1
        if not count == int(found.split('/')[0]):
            print(item[0])
            print(f_apis)
            print(m_apis)

print(sum_df)
print(sum_index)
sum_df.to_excel("summary_set3.0.xlsx", index = False)
print(f"Total Privacy APIs in docs: {total_APIs}")
print(f"Correctly Found Privacy APIs: {correct_found_APIs}")
print(f"coverage rate: {correct_found_APIs/total_APIs}")
print(f"Total Found Privacy APIs: {found_APIs}")
print(f"False Positive Count: {FP_count}")
print(f"FP rate: {FP_count/found_APIs}")