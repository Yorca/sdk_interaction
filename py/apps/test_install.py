import subprocess
import os
import time


import os
import subprocess
import time

import frida
import json
from datetime import datetime
import zipfile
import re

def extract_xapk(xapk_file, output_dir):
    """Extracts the XAPK file and returns the extracted file name."""
    if zipfile.is_zipfile(xapk_file):
        with zipfile.ZipFile(xapk_file, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
            extracted_files = zip_ref.namelist()  # List of all extracted files
            print(f"Extracted {xapk_file} to {output_dir}")
            return extracted_files  # Return the list of extracted file names
    else:
        print(f"{xapk_file} is not a valid XAPK file.")
        return None




def push_obb(obb_files, package_name):
    """Pushes OBB files to the device."""
    obb_destination = f"/sdcard/Android/obb/{package_name}/"
    print(f"Creating OBB directory: {obb_destination}")
    subprocess.run(["adb", "shell", "mkdir", "-p", obb_destination])
    for obb_file in obb_files:
        print(f"Pushing OBB file: {obb_file}")
        subprocess.run(["adb", "push", obb_file, obb_destination])
    print("OBB files transferred successfully.")

def installApk(path, pkg_name, file_path):
    try:
        if file_path.endswith('.apk'):
            res = subprocess.run(["adb", "install", file_path])
            return res.returncode == 0
        else:
            xapk_path = os.path.join(f"{path}/apk_extract", pkg_name)
            apk_files = extract_xapk(file_path, xapk_path)
            apk_files = [file for file in apk_files if file.endswith('.apk')]
            obb_files = [file for file in apk_files if file.endswith('.obb')]
            apk_paths = [f"{xapk_path}/{file}" for file in apk_files]
            command = ["adb", "install-multiple"]
            command += apk_paths
            result = subprocess.run(command)
            print(f"install result = {result}")
            if result.returncode == 0:
                if obb_files:
                    push_obb(obb_files, pkg_name)
                return True
            return False

    except Exception as e:
        print(f"error : {e}")
        return False

source = "/Volumes/T7 Shield/apps"
success_count = 0
failed_count = 0
with open("install/success2.txt", "r") as file:
    success_apks = [apk.replace("\n", "") for apk in file.readlines()]
with open("install/failed2.txt", "r") as file:
    failed_apks = [apk.replace("\n", "") for apk in file.readlines()]


for filename in os.listdir(source):
    # if filename in success_apks or filename in failed_apks:
    #     print(filename)
    #     continue
    print(filename)
    if filename.endswith('XAPK') or filename.endswith('APK'):
        print(filename)
    path = os.path.join(source, filename)
    pkg_name = filename.removesuffix(".xapk").removesuffix('.apk')
    print(pkg_name)

    if installApk(source, pkg_name, path):
        print(f"{filename} succeeded")
        success_count += 1
        subprocess.run(["adb", "uninstall", pkg_name])
        with open("install/success2.txt", "a") as file:
            file.write(f"{filename}\n")
    else:
        failed_count += 1
        with open("install/failed2.txt", "a") as file:
            file.write(f"{filename}\n")
        print(f"{filename} failed")
print(success_count)
print(failed_count)

