import pandas as pd
import json
summary_version = "md_merge"
data = pd.read_excel(f'Summary Evaluation3.0.xlsx')
sum = 0
for index, row in data.iterrows():
    sdk_name = row[0]
    with open(f"summary/merged/{sdk_name}.json") as file:
        file_data = file.read()
        summary = json.loads(file_data)
    apis = []
    print(summary)
    for api in summary["privacy_APIs"]:
        apis.append(api["API_name"])
    sum += len(set(apis))
    data.at[index, "APIs from Summary"] = ', '.join(apis)
    # data.at[index, "Summary"] = file_data

print(data)
data.to_excel(f'Updated_Summary_Evaluation{summary_version}.xlsx', index=False)

print(sum)