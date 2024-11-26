import json

with open("data/classes_in_packages.json", "r") as file:
    data = json.load(file)

new_data = {}
for key in data.keys():
    pkg = key.replace(".apk.packages", "").replace(".xapk.packages", "")
    new_data[pkg] = data[key]

with open("data/classes_in_packages_new.json", "a") as file:
    file.write(json.dumps(new_data, indent=4))
