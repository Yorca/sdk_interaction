# import os
# import json
#
# log_path = "../Dynamic/log/apk_log"
#
# with open("../Dynamic/data/api_summary_groundtruth.json", "r") as file:
#      data = json.load(file)
#
# res = []
#
# for sdk in data["LIBS"]:
#      for api in sdk['privacy_APIs']:
#           if "parameter_configurations" not in api.keys() or len(api["parameter_configurations"]) == 0:
#                res.append({
#                     "SDK": sdk["SDK"],
#                     "class_name": api["class_name"],
#                     "API": api['API_name'],
#                     "has_param": False,
#                     "params_in_log": []
#                })
#           else:
#                res.append({
#                     "SDK": sdk["SDK"],
#                     "class_name": api["class_name"],
#                     "API": api['API_name'],
#                     "has_param": True,
#                     "params_in_sum": [param['parameter_values'] for param in api["parameter_configurations"]],
#                     "params_in_log": []
#                })
#
#
#
# for filename in os.listdir(log_path):
#      if filename.startswith('.'):
#           continue
#      path = os.path.join(log_path, filename)
#      with open(path, "r") as file:
#           data = "[" + file.read()[:-2] + "]"
#
#           data = json.loads(data)
#
#      for item in data:
#           if not item["is_privacy"]:
#                continue
#           for api in res:
#                if item["method"] == api['API'] and item["class_name"] in api["class_name"] and not item['arguments'] in api['params_in_log']:
#                     api['params_in_log'].append(item['arguments'])
#                     if "myUSPrivacyString" in item['arguments']:
#                         print(item)
#                         print(log_path)
#                continue
# with open("data/para_map2.log", "w") as file:
#      file.write(json.dumps(res, indent=4))
from difflib import SequenceMatcher
import json
def get_closest_string(target, string_list):
    """
    Find the closest string in the list to the target string.

    Args:
        target (str): The string to compare against.
        string_list (list): A list of strings to find the closest match.

    Returns:
        str: The closest string from the list.
    """
    if not string_list:
        return None

    # Use SequenceMatcher to calculate similarity
    closest_string = max(string_list, key=lambda x: SequenceMatcher(None, target, x).ratio())
    return closest_string
with open("data/para_map2.log", "r") as file:
     data = json.load(file)
for item in data:
     match_res = {}
     for param in item["params_in_log"]:
          if "params_in_sum" in item.keys():
               sum_params = [str(p) for p in item["params_in_sum"]]
               match_res[str(param)] = get_closest_string(str(param), sum_params)
     item["mathes"] = match_res
print(data)

with open("data/param_map_res_2.json", "w") as file:
     file.write(json.dumps(data, indent=4))


