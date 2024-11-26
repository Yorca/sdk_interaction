# import os
# import env
# import json
# import tools
# def get_api_trace(pkg_name):
#     path = os.path.join(env.apk_log_folder, pkg_name + ".log")
#     if not os.path.exists(path):
#         return None, False
#     print(f"start {pkg_name}")
#     with open(path) as file:
#         data = "[" + file.read()[:-2] + "]"
#     data = json.loads(data)
#     fields_to_keep = {"method", "class_name", "timestamp", "arguments", "is_privacy", "return", "source"}
#     filtered_data = [{k: v for k, v in item.items() if k in fields_to_keep} for item in data]
#
#     has_privacy_api = False
#     has_sensitive_api = False
#     new_trace = []
#     for trace in filtered_data:
#         if trace["is_privacy"]:
#             has_privacy_api = True
#             new_trace.append(trace)
#
#     if has_privacy_api:
#         print(f"has privacy api: {pkg_name}")
#     return "YES", has_privacy_api
#
# with open("../apps/install/success.txt", "r") as file:
#     success_apks = file.readlines()
# pkg_list = [apk.replace(".apk\n", "") for apk in success_apks]
# count = 0
# privacy_count = 0
# for pkg in pkg_list:
#     trace, has = get_api_trace(pkg)
#     if trace:
#         count += 1
#     if has:
#         privacy_count += 1
# print(count)
# print(privacy_count)
import os

total = 0
pri = 0

for filename in os.listdir("../Dynamic/log/apk_log"):
    path = os.path.join("../Dynamic/log/apk_log", filename)
    if not filename.endswith('.log'):
        continue
    with open(path, "r") as file:
        data = file.read()
    total += 1
    pattern = '"is_privacy": true'
    if pattern in data.lower():
        pri += 1
        print(filename)
print(f"{pri}/{total}")
#/Users/yorca/Downloads/classes_in_packages2.txt
# import json
# import os
# with open("../Dynamic/data/classes_in_packages_new.json", "r") as file:
#     data = json.load(file)
# for key in data.keys():
#     if "com.facebook.ads.AdSettings".lower() in data[key].lower() and "com.applovin.sdk.AppLovinPrivacySettings".lower() in data[key].lower():
#             print(key)
#
#
# with open("/Users/yorca/Downloads/classes_in_packages2.txt", "r") as file:
#     lines = file.readlines()
# for line in lines:
#     if "com.facebook.ads.AdSettings".lower() in line.lower() and "com.applovin.sdk.AppLovinPrivacySettings".lower() in line.lower():
#             print(line.split(':')[0])

