
import os
import subprocess
for filename in os.listdir("/Volumes/Yorca_T7/apps/8773apps"):

    pck_name = filename.removesuffix(".apk")
    print(pck_name)

    print(pck_name)
    res = subprocess.run(["adb", "uninstall", pck_name])
    print(res)