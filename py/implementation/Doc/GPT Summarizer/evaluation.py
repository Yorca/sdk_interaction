import pandas as pd
import json
data = pd.read_excel('Summary Evaluation.xlsx')

sum = 0
for index, row in data.iterrows():
    sdk_name = row[0]
    with open(f"summaries2.0/{sdk_name}.json") as file:
        file_data = file.read()
        summary = json.loads(file_data)
    apis = []
    for api in summary["privacy_APIs"]:
        apis.append(api["API_name"])
    sum += len(apis)
    data.at[index, 3] = ', '.join(apis)
    data.at[index, "Summary"] = file_data

print(data)
data.to_excel('Updated_Summary_Evaluation.xlsx', index=False)

print(sum)