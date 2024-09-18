import pandas as pd

with open("app_metadata_topfree.csv", "r") as file:
    lines = file.readlines()
for line in lines:
    print(line)
data = pd.read_csv("app_metadata_topfree.csv")
print(data)
# merged_data = data.groupby(['appId'], as_index=False).agg({'type': ', '.join})
