import json
import os

import pandas as pd

source_dir = "summary/filtered"

api_list = []
df = pd.DataFrame(columns=["SDK", "API", "class"])
for filename in os.listdir(source_dir):
    print(filename)
    with open(os.path.join(source_dir, filename), "r") as file:
        data = file.read()

    js_data = json.loads(data)
    for api in js_data["privacy_APIs"]:
        df.loc[len(df)] = [filename.replace(".json", ""), api["API_name"], ','.join(api["class_name"])]
df.to_csv("data/privacy_apis.csv", index=False)
