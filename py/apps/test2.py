import pandas as pd
data = pd.read_csv("app_metadata_topfree.csv")
print(len(data))
idlist = []
for index, row in data.iterrows():
    idlist.append(row[0].rstrip('"'))
idlist = list(set(idlist))
print(len(idlist))
merged_data = data.groupby(['appId', 'title'], as_index=False).agg({'type': ', '.join})
merged_data[merged_data.columns[0]] = merged_data[merged_data.columns[0]].apply(lambda x: x.rstrip('"') if isinstance(x, str) else x)
print(merged_data[:5])
merged_data.to_csv("app_metadata_topfree_merged.csv", index=False)