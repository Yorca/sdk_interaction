import json

#
# def deleteDuplicate(list_of_dicts):
#     unique_list = [dict(t) for t in {tuple(sorted(d.items())) for d in list_of_dicts}]
#     return unique_list

with open("data/api_summary_groundtruth.json", "r") as file:
    data = json.loads(file.read())


sdks = data["LIBS"]
count = 0
api_list = []
cls_list = []
for sdk in sdks:
    sdk_name = sdk["SDK"]
    apis = sdk["privacy_APIs"]
    if "classes" in sdk:
        sdk_cls_for_hook = sdk["classes"]
        for cls in sdk_cls_for_hook:
            cls_list.append(cls)

    for api in apis:
        count +=1
        api_name = api["API_name"]
        cls = api["class_name"]
        for cls_name in cls:
            item = {
                "SDK": sdk_name,
                "API": api_name,
                "Class": cls_name
            }
            if "privacy_params" in api.keys():
                item["privacy_params"] = api["privacy_params"]
            api_list.append(item)
            cls_list.append(cls_name)

apis_js = json.dumps(api_list, indent=4)
with open("data/apis_v3.json", "w") as file:
    file.write(apis_js)
cls_list = list(set(cls_list))
cls_js = json.dumps(cls_list, indent=4)
# with open("data/classes.json", "w") as file:
#     file.write(cls_js)