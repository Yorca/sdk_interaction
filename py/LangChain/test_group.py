import json
import os

path = "../Dynamic/log/apk_log"

def get_prefix(class_name):
    components = class_name.split('.')
    if len(components) >= 2:
        return '.'.join(components[:2])
    return None

for filename in os.listdir(path):
    if not filename.endswith('.log') or filename.startswith('.'):
        continue
    file_path = os.path.join(path, filename)
    with open(file_path, 'r') as file:
        data = json.load(file)

    total_count = 0
    remove_count = 0
    for i in range(len(data)):
        api = data[i]
        if api['is_privacy']:
            prefixs = [get_prefix(api['class_name'])]
            for j in range(i + 1,len(data)):
                total_count += 1
                sub_api = data[j]
                connected = False
                for prefix in prefixs:
                    if prefix in sub_api["stack_trace"]:
                        prefixs.append(get_prefix(sub_api["class_name"]))
                        prefixs = list(set(prefixs))
                        connected = True
                        break
                if not connected:
                    remove_count += 1


print(f"{remove_count}/{total_count}")


