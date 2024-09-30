import json
import subprocess
import os
import re
import pandas as pd

api_set_data = pd.read_excel("apis_set.xlsx")
apis = []
for _, row in api_set_data.iterrows():
    apis.append(row[1])
apis = list(set(apis))

apis.remove("init")
apis.remove("reset")
apis.remove("initialize")
apis.remove("setParam")
apis.remove("start")
apis.remove("pause")
apis.remove("resume")
apis.remove("ask")
apis.remove("edit")
apis.remove("GPP")
apis.remove("CMP")
apis.remove("block")

def decompile_apk(apk_path):
    output_dir = apk_path + "_decompiled"
    if os.path.exists(output_dir):
        return output_dir
    subprocess.run(["apktool", "d", apk_path, "-o", output_dir], check=True)
    return output_dir


def search_method_in_files(root_dir, filename):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".smali"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    cls_name = ""
                    for line in lines:
                        if line.startswith(".class"):
                            cls_name = line.split(" ")[-1]
                            cls_name = cls_name[1:-2]
                            cls_name = cls_name.replace('/', '.')
                        elif line.startswith('.method'):
                            mtd = line.split('(')[0].split(' ')[-1]
                            if mtd in apis:
                                with open(f"res/{mtd}.json", "r") as f:
                                    api_data = f.read()
                                    print(api_data)
                                    js_data = json.loads(api_data)
                                    if cls_name not in js_data.keys():
                                        js_data[cls_name] = [filename]
                                    elif filename not in js_data[cls_name]:
                                        js_data[cls_name].append(filename)
                                with open(f"res/{mtd}.json", "w") as f:
                                    f.write(json.dumps(js_data, indent=4))

def configApis(apis):
    for api in apis:
        with open(f"res/{api}.json", "w") as file:
            file.write(json.dumps({}, indent=4))



def main(apk_path, filename):
    decompiled_dir = decompile_apk(apk_path)
    search_method_in_files(decompiled_dir, filename)

apk_dir = "/Volumes/YorcaDisk/class_apks"
configApis(apis)
for filename in os.listdir(apk_dir):
    if not filename.lower().endswith(".apk") and not filename.lower().endswith(".xapk"):
        continue
    apk_path = os.path.join(apk_dir, filename)
    main(apk_path,filename)

