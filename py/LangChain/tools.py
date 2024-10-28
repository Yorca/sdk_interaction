from langchain.tools import Tool
import json
import env
summary_ground_truth = env.summary_ground_truth

def get_all_privacy_apis():
    all_apis = []
    with open(summary_ground_truth, "r") as file:
        data = json.loads(file.read())
    for sdk in data["LIBS"]:
        for api in sdk["privacy_APIs"]:
            all_apis += [f"{cls};{api['API_name']}" for cls in api["class_name"] if api["class_name"]]
    return all_apis

def is_privacy_api(cls, mtd):
    apis = get_all_privacy_apis()
    for api in apis:
        if cls == api.split(";")[0] and mtd == api.split(";")[1]:
            return "it is a privacy API"
    return "it is not a privacy API"

privacy_api_checker = Tool (
    func=is_privacy_api,
    description="This tool checks whether the method in the class is a privacy API in our database.",
    name="PrivacyApiCheckTool"
)