import os
import zipfile
import subprocess
import sys

def extract_xapk(xapk_file, extract_path):
    """Extracts the XAPK file to the specified directory."""
    with zipfile.ZipFile(xapk_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print(f"Extracted '{xapk_file}' to '{extract_path}'")

def install_apk(apk_path):
    """Installs the APK on the connected Android device."""
    print(f"Installing APK: {apk_path}")
    result = subprocess.run(["adb", "install-multiple", apk_path], capture_output=True, text=True)
    if result.returncode == 0:
        print("APK installed successfully.")
    else:
        print(f"Failed to install APK. Error: {result.stderr}")
        sys.exit(1)

def push_obb(obb_files, package_name):
    """Pushes OBB files to the device."""
    obb_destination = f"/sdcard/Android/obb/{package_name}/"
    print(f"Creating OBB directory: {obb_destination}")
    subprocess.run(["adb", "shell", "mkdir", "-p", obb_destination])
    for obb_file in obb_files:
        print(f"Pushing OBB file: {obb_file}")
        subprocess.run(["adb", "push", obb_file, obb_destination])
    print("OBB files transferred successfully.")

def get_package_name(apk_paths):
    """Retrieves the package name from the APK using aapt."""
    for apk_path in apk_paths:
        print("Retrieving package name from APK.")
        result = subprocess.run(["aapt", "dump", "badging", apk_path], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if "package: name=" in line:
                return line.split("'")[1]

def main():
    xapk_file = "/Users/yorca/Downloads/test/Google Chrome_130.0.6723.86_APKPure.xapk"  # Replace with your .xapk file path
    extract_path = "../extracted_xapk"

    extract_xapk(xapk_file, extract_path)

    # Find APK and OBB files
    apk_files = []
    obb_files = []
    for root, dirs, files in os.walk(extract_path):
        for file in files:
            if file.endswith('.apk'):
                apk_file = os.path.join(root, file)
                apk_files.append(apk_file)
            elif file.endswith('.obb'):
                obb_files.append(os.path.join(root, file))

    if not apk_files:
        print("APK file not found in the XAPK package.")
        sys.exit(1)

    package_name = get_package_name(apk_files)
    print(package_name)
    print(apk_file)
    install_apk(apk_file)

    if obb_files:
        push_obb(obb_files, package_name)
    else:
        print("No OBB files to transfer.")

if __name__ == "__main__":
    main()
