import subprocess
import os
import time

source = "/Volumes/Yorca_T7/apps/8773apps"
success_count = 0
failed_count = 0
for filename in os.listdir(source):
    path = os.path.join(source, filename)
    pkg_name = filename.rstrip(".apk")
    print(pkg_name)
    res = subprocess.run(["adb", "install", path])
    if res.returncode == 0:
        print(f"{filename} succeeded")
        success_count += 1
        subprocess.run(["adb", "uninstall", pkg_name])
        with open("install/success.txt", "a") as file:
            file.write(f"{filename}\n")
    else:
        failed_count += 1
        with open("install/failed.txt", "a") as file:
            file.write(f"{filename}\n")
        print(f"{filename} failed")
print(success_count)
print(failed_count)

