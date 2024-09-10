from openai import OpenAI
from bs4 import BeautifulSoup
import os
import json

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def read_and_parse_html(file_path):
    # Read your HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse HTML using Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Example: Extract text or specific elements
    text_content = soup.get_text(separator=' ', strip=True)
    return text_content

sys_prompt = """

You will receive a documentation and a target API. Your task is to summarize the target API based on the document using the following format. 

Tips:
1. Do not infer what is not in the documentation 
2.Please strictly adhere to the format 
3.If you cannot extract the corresponding information from the document, you may leave the item blank. 
4. You can extend the format to cover important information or specifications if necessary. 
5. The annotations after each item imply what should be filled in.
6. value in list format([]) implies it may have one or multiple results.
7. You have to include all important details related to the target API

format
{
    "SDK_name": "", // the name of the SDK
    "API_name": "", // the name of the target API
    "target_key_index": "", // for an API like set(key, value), and we only target the scenario when key == target_key_name
    "target_key_name": "", // for an API like set(key, value), the index of the key parameter
    "effects": [], // What functionalities does the API have (What happens after calling the API).
    "preconditions": [], // pre condtions of the API
    "postconditions": [], // postcondition of the API
    "invariants": [], // invariants of the API
    "requirements":[],// extra conditions or requirements of calling the API
    "parameters": [ // summary of all parameters; if no parameters in the API, leave it blank
      {
        "index": 0, // the index of the parameter in the method
        "rules": [{ // all possible values for the parameters, and the config rules
          "value": "", // one value that can be assigned to the parameter
          "effects": [], // If the parameter is assigned this value, what will happen
          "preconditions": [], // pre condtions of setting the parameter to this value
          "postconditions": [], // post condtions of setting the parameter to this value
          "invariants": [], // invariants of setting the parameter to this value
          "requirements":[]// extra requirements of setting the parameter to this value
        },
        {
          "value": "", 
          "effects": [],
          "preconditions":[], 
          "postconditions": [],
          "invariants": [],
          "requirements": []
        }]
      }
    ]
  }
"""

# user_prompt = f"""
#   documentation:
#   {read_and_parse_html("/Users/yorca/PycharmProjects/website_archive/website_html/Ironsource_gdpr_ccpa_coppa.pdf.html")}
#
#   Target API: setMetaData(), key = "is_child_directed"
# """


# print(user_prompt)

def analyze(user_prompt, sdk, api):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    res = []
    for choice in completion.choices:
        res.append(str(choice.message.content))

    with open(f"responses/{sdk}_{api}.json", 'w') as file:
        json.dump(res, file, indent=4)

def analzed_with_type(apis, type, analyzed_apis):
    # apis = sdks[sdk]["gdpr"]
    for api in apis:
        if isinstance(api, dict) and "apiMethodName" in api.keys():
            targer_api = api["apiMethodName"]
            file_paths = search_doc(sdk, type)
            if targer_api in analyzed_apis or len(file_paths) == 0 or has_analyzed(sdk, targer_api):
                continue

            index = 0
            user_prompt = ""
            for file_path in file_paths:
                index += 1
                user_prompt += f"""
                Document{index}:
                {read_and_parse_html(file_path)}
                """
            user_prompt += f"""
            target API: {targer_api}
            """

            print(user_prompt)
            try:
                analyze(user_prompt, sdk, targer_api)
            except:
                print(f"analyze {sdk} {targer_api} error")
            analyzed_apis.append(targer_api)

def search_doc(sdk, type):
    folder = "website_html"
    file_paths = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if sdk in file and type in file:
                file_paths.append(f"{folder}/{file}")
    return file_paths


def has_analyzed(sdk, api):
    folder = "responses"
    for root, dirs, files in os.walk(folder):
        for file in files:
            if sdk in file and api in file:
                return True
    return False

with open("Priv_impl.json", "r") as file:
    data = file.read()

sdks = json.loads(data)

for sdk in sdks.keys():
    analyzed_apis = []
    analzed_with_type(sdks[sdk]["gdpr"], "gdpr", analyzed_apis)
    analzed_with_type(sdks[sdk]["us_p"], "ccpa", analyzed_apis)
    analzed_with_type(sdks[sdk]["coppa"], "coppa", analyzed_apis)
    #
    # gdprs = sdks[sdk]["gdpr"]
    # for gdpr in gdprs:
    #     if isinstance(gdpr, dict) and "apiMethodName" in gdpr.keys():
    #         targer_api = gdpr["apiMethodName"]
    #         file_paths = search_doc(sdk, "gdpr")
    #         if targer_api in analyed_apis or len(file_paths) == 0:
    #             continue
    #
    #         index = 0
    #         user_prompt = ""
    #         for file_path in file_paths:
    #             index += 1
    #             user_prompt += f"""
    #             Document{index}:
    #             {read_and_parse_html(file_path)}
    #             """
    #         user_prompt += f"""
    #         target API: {targer_api}
    #         """
    #
    #         print(user_prompt)
    #       #  analyze(user_prompt, sdk, targer_api)
    #         analyed_apis.append(targer_api)











