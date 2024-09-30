import json
import subprocess
import os
import re
import pandas as pd
import threading

# Initialize a lock object
file_lock = threading.Lock()

# Load API data
api_set_data = pd.read_excel("apis_set.xlsx")
apis = list(set(api_set_data.iloc[:, 1]))
apis = [api for api in apis if
        api not in ["init", "reset", "initialize", "setParam", "start", "pause", "resume", "ask", "edit", "GPP", "CMP",
                    "block"]]


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
                            cls_name = line.split(" ")[-1][1:-2].replace('/', '.')
                        elif line.startswith('.method'):
                            mtd = line.split('(')[0].split(' ')[-1]
                            if mtd in apis:
                                with file_lock:  # Lock for thread-safe file reading and writing
                                    with open(f"res/{mtd}.json", "r") as f:
                                        api_data = f.read()
                                    js_data = json.loads(api_data)

                                    if cls_name not in js_data:
                                        js_data[cls_name] = [filename]
                                    elif filename not in js_data[cls_name]:
                                        js_data[cls_name].append(filename)

                                    with open(f"res/{mtd}.json", "w") as f:
                                        f.write(json.dumps(js_data, indent=4))


def configApis(apis):
    with file_lock:
        for api in apis:
            with open(f"res/{api}.json", "w") as file:
                file.write(json.dumps({}, indent=4))


def process_apk(apk_path, filename):
    decompiled_dir = decompile_apk(apk_path)
    search_method_in_files(decompiled_dir, filename)


def main():
    apk_dir = "/Volumes/YorcaDisk/class_apks"
    configApis(apis)

    threads = []

    for filename in os.listdir(apk_dir):
        if not filename.lower().endswith((".apk", ".xapk")):
            continue
        apk_path = os.path.join(apk_dir, filename)

        # Create a new thread for each APK processing task
        thread = threading.Thread(target=process_apk, args=(apk_path, filename))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
