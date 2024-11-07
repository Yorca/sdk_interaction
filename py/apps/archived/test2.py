import os

dataset_dirs = ["/home/zh844971/sdk_interaction/apk_downloader_2",
                "/home/zh844971/sdk_interaction/apks1",
                "/home/zh844971/sdk_interaction/apks3",
                "/home/zh844971/sdk_interaction/apks_macmini",
                "/home/zh844971/sdk_interaction/apks_macpro",
                "/home/zh844971/sdk_interaction/sdk_interaction/py/apk_downloader/apks",
                "/home/zh844971/sdk_interaction/sdk_interaction/py/apk_downloader/apks1",
                "/home/zh844971/sdk_interaction/sdk_interaction/py/apk_downloader/apks_new"]
downloaded_apks = []
for dir in dataset_dirs:
    for filename in os.listdir(dir):
        if not filename.lower().endswith(".xapk") and not filename.lower().endswith(".apk"):
            continue
        pkg_name = ""
        if "---" in filename:
            pkg_name = filename.split("---")[0]
        elif "_apkpure" not in filename.lower():
            pkg_name = filename.rsplit('_', 1)[0]
        else:
            pkg_name = filename.split('_')[0]
        file_path = os.path.join(dir, filename)
        if os.path.getsize(file_path) > 1 * 1024 * 1024:
            downloaded_apks.append(pkg_name)
        else:
            with open("small_apks2.txt", "a") as file:
                file.write(f"{pkg_name};{filename}\n")

downloaded_apks = list(set(downloaded_apks))
print(f"total {len(downloaded_apks)}")
downloaded_apks = [f"{apk}\n" for apk in downloaded_apks]
with open("downloaded_pkg2.txt", "a") as file:
    file.writelines(downloaded_apks)

