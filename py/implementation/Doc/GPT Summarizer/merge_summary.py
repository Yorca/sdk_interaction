import json
import os
sum_directory = "summary"
doc_source = f"../web_archive/privacy_doc_md_final/"
from collections import defaultdict


def merge_list(data, target_key):
    new_list = {}
    for item in data:
        new_key = str(item[target_key])
        if new_key not in new_list.keys():
            for key in item.keys():
                if not key == target_key and not isinstance(item[key], list):
                    item[key] = [item[key]]
            new_list[new_key] = item
        else:
            target_item = new_list[new_key]
            for key in item.keys():
                if not key == target_key:
                    if isinstance(item[key], list):
                        target_item[key] += item[key]
                    else:
                        target_item[key].append(item[key])
                    try:
                        target_item[key] = list(set(target_item[key]))
                    except:
                        pass

    return [new_list[key] for key in new_list.keys()]




for sdk in os.listdir(doc_source):
    api_data = []
    for i in range(1,6):
        des_path = f"summary/sum{i}/{sdk}.json"
        if not os.path.exists(des_path):
            continue
        with open(des_path, 'r') as file:
            sum_data = file.read()
        js_data = json.loads(sum_data)
        api_data += js_data['privacy_APIs']
    # print(merge_list(api_data, "API_name"))
    merged_data = merge_list(api_data, "API_name")
    for item in merged_data:
        item["parameter_configurations"] = merge_list(item["parameter_configurations"], "parameter_values")
    print(merged_data)
    dump_data = {
        "SDK": sdk,
        "privacy_APIs": merged_data
    }
    json_data = json.dumps(dump_data, indent=4)
    with open(f"summary/merged/{sdk}.json", 'w') as file:
        file.write(json_data)