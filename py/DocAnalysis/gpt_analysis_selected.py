from openai import OpenAI
from bs4 import BeautifulSoup
import os
import json

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response_folder = "response_selected"
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

I will give you a document which may contain one or more privacy-related APIs, your task is to:
1. Locate these APIs from the document
2. Find all related (directly or indirectly) texts about the API. 
3. Based on the texts, extract summaries of these privacy APIs using the provided format.

An API is considered a privacy API if it is clearly privacy-related, or if it meets any of the following criteria:

1. Data Access and Handling:
    1.1 Personal Data: Does the API access, collect, store, or process personal data such as names, addresses, email addresses, phone numbers, ID numbers, etc.?
    1.2 Sensitive Information: Does the API handle sensitive information such as biometric data (fingerprints, facial recognition), health data, financial information, etc.?
    1.3 Sensitive device permissions: Does the API collect or handle sensitive device data such as location, contacts, SMS, device identification information (device ID, Andorid ID, Adverstising ID, etc.), etc?
2. Data Transmission and Storage:
    2.1 Encryption: Does the API use encryption technologies (e.g., HTTPS, encryption libraries) to protect data during transmission and storage?
    2.2 Data Storage Location: Does the API specify where data is stored and ensure compliance with relevant privacy laws and regulations?
3. User Control and Consent:
    3.1User Consent: Does the API obtain explicit user consent before collecting or processing data, and allow users to withdraw consent at any time?
    3.2Data Access and Deletion: Does the API provide mechanisms for users to access their data and delete their personal information?
4. Transparency and Policy:
    4.1Privacy Policy: Is there a detailed privacy policy associated with the API, explaining how data is collected, used, and shared?
    4.2 Data Sharing: Does the API involve sharing user data with third parties, and are users clearly informed about this sharing?
5. Data Minimization and Purpose Limitation:
   5.1 Data Minimization: Does the API collect and process only the minimum amount of data necessary to achieve its function?
    5.2 Purpose Limitation: Is the use of the data clearly defined, ensuring that it is not used for unauthorized purposes?
6. Privacy Law Compliance:
     6.1 Is the API designed for compliance requirements of privacy regulations or laws?
    

Instructions for summarizing an API:

1. Do not infer what is not included in the documentation, but you can use your prior knowledge to make the description more specific
2. You have to include all important details related to the target API. 
3. Descriptions of the API might be referenced in different parts of the documentation, not only in the API section, you need to find all related information.
4. Please strictly adhere to the following format. The annotations after each item imply what should be filled in. If you cannot extract the corresponding information from the document, you may leave the item blank.

[{
    "SDK_name": "", // The name of the SDK
    "API_name": "", // The name of the target API
    "conditions": [], // The list of conditions required to call the API
    "effects": [], // The list of effects and consequences of calling the API
    "parameter_configuations": [ // Summary of all configurable parameters or parameter combinations; if no parameters in the API, leave it blank. 
      {
	      parameter_values:[], // One of the parameter combinations that are mentioned in the document. If some parameter is not configuable or unknown, mark it "null" in the corresponding index in the list.
	      conditions:[], // The list of conditions or requirements of setting parameters to parameter_values
	      effects:[], // The list of effects or consequences of setting parameters to parameter_values 
      }
    ]
  }]
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
    actual_json_str = json.loads(res[0])

    beautified_json = json.dumps(actual_json_str, indent=4)
    with open(f"{response_folder}/{sdk}_{api}.json", 'w') as file:
        file.write(beautified_json)

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

            # print(user_prompt)
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
    for root, dirs, files in os.walk(response_folder):
        for file in files:
            if sdk in file and api in file:
                return True
    return False

with open("Priv_impl.json", "r") as file:
    data = file.read()

sdks = json.loads(data)

for sdk in sdks.keys():
    if sdk.lower() not in ["appodeal", "applovin", "admob", "inmobi", "vungle", "ironsource"]:
        continue
    print("start analyze " + sdk)
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











