# import json
# import os
#
# path = "../Dynamic/log/apk_log"
#
# def get_prefix(class_name):
#     components = class_name.split('.')
#     if len(components) >= 2:
#         return '.'.join(components[:2])
#     return None
#
# for filename in os.listdir(path):
#     if not filename.endswith('.log') or filename.startswith('.'):
#         continue
#     file_path = os.path.join(path, filename)
#     print(file_path)
#     with open(file_path, 'r') as file:
#         data = "[" + file.reads()[:-1] + "]"
#         data = json.load(file)
#
#     total_count = 0
#     remove_count = 0
#     for i in range(len(data)):
#         api = data[i]
#         if api['is_privacy']:
#             prefixs = [get_prefix(api['class_name'])]
#             for j in range(i + 1,len(data)):
#                 total_count += 1
#                 sub_api = data[j]
#                 connected = False
#                 for prefix in prefixs:
#                     if prefix in sub_api["stack_trace"]:
#                         prefixs.append(get_prefix(sub_api["class_name"]))
#                         prefixs = list(set(prefixs))
#                         connected = True
#                         break
#                 if not connected:
#                     remove_count += 1
#
#
# print(f"{remove_count}/{total_count}")
with open('stat.txt', 'r') as file:
    data = file.read().split('\n')

count = 0
total = 0
for item in data:
    if '/' not in item:
        continue
    count += int(item.removeprefix('remove ').strip().split('/')[0])
    total += int(item.removeprefix('remove ').strip().split('/')[1])
print(f"{count}/{total}")
# import json
#
# with open("../Dynamic/data/classes_in_packages_5000.json", 'r') as file:
#     data = json.load(file)
#
# count = 0
# total = 0
# for key in data.keys():
#
#     if 'applovin' in data[key].lower() and 'appodeal' in data[key].lower():
#         print(key)
#         pkg = '.'.join(key.split('.')[:-2])
#         with open(f'../apps/app_details_5000/{pkg}', 'r') as file:
#             js_data = json.load(file)
#             print(js_data['realInstalls'])
#         count += 1
#     total += 1
# print(count)
# print(total)
