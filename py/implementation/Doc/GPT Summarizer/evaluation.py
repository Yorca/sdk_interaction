import pandas as pd
import json
summary_version = "3.0"
data = pd.read_excel(f'Summary Evaluation{summary_version}.xlsx')
sum = 0
for index, row in data.iterrows():
    sdk_name = row[0]
    with open(f"summaries{summary_version}/{sdk_name}.json") as file:
        file_data = file.read()
        summary = json.loads(file_data)
    apis = []
    for api in summary["privacy_APIs"]:
        apis.append(api["API_name"])
    sum += len(apis)
    data.at[index, "APIs from Summary"] = ', '.join(apis)
    # data.at[index, "Summary"] = file_data

print(data)
data.to_excel(f'Updated_Summary_Evaluation{summary_version}.xlsx', index=False)

print(sum)