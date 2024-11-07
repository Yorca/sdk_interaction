with open("../data/app_metadata_topfree-100.csv", "r") as file:
    lines = file.readlines()


import pandas as pd

data = pd.read_csv("../data/app_metadata_topfree_merged.csv")

pkgs = [row[0] for _,row in data.iterrows()]
missed = []
for line in lines[1:]:

    [pkg, name, type] = line.replace('"', "").split(',')
    if pkg not in pkgs:
        missed.append(pkg)
missed = list(set(missed))
print(len(missed))


