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
        return False

    except Exception as e:
        return False

source = "/Volumes/Yorca_T7/apps/xapks"
success_count = 0
failed_count = 0
for filename in os.listdir(source):
    path = os.path.join(source, filename)
    pkg_name = filename.rstrip(".xapk")
    print(pkg_name)
    if installApk(source, pkg_name, path):
        print(f"{filename} succeeded")
        success_count += 1
        subprocess.run(["adb", "uninstall", pkg_name])
        with open("install/xapk_success.txt", "a") as file:
            file.write(f"{filename}\n")
    else:
        failed_count += 1
        with open("install/xapk_failed.txt", "a") as file:
            file.write(f"{filename}\n")
        print(f"{filename} failed")
print(success_count)
print(failed_count)

