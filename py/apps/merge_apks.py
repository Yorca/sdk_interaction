import os
import shutil

def pckNameParttern1(filename):
    return filename.split("---")[0]


def pckNameParttern2(filename):
    return filename.split("_")[0]


def copy_apk_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if filename.endswith((".apk", ".xapk")):
            file_path = os.path.join(source_folder, filename)
            pkg_name = pckNameParttern1(filename)
            if os.path.getsize(file_path) > 1 * 1024 * 1024:
                shutil.copy(file_path, destination_folder)
                with open("merge_success.txt", "a") as file:
                    file.write(f"{pkg_name}\n")
            else:
                with open("merge_fail.txt", "a") as file:
                    file.write(f"{pkg_name}\n")


source_folder = "/home/zh844971/sdk_interaction/apk_downloader_2"
destination_folder = "/home/zh844971/sdk_interaction/apks_merge"
copy_apk_files(source_folder, destination_folder)