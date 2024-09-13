from openai import OpenAI
from bs4 import BeautifulSoup
import os
import json
import email
from html.parser import HTMLParser
from datetime import datetime

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

summary_version = "md"
errorlog_name = f"log/error_log_md.log"
sys_prompt = """
You are a Privacy API Summarizer. You will be provided with a document that may contain one or several privacy-related APIs. Your task is to:
1. Identify all privacy-related APIs within the document.
2. Gather all relevant inforamtion about these privacy API(s).
3. Extract and Summarize the information regarding these privacy APIs using the provided format.
Definition of a Privacy API:
An API is considered a privacy API if it is explicitly privacy-related, or if it involves:
1. Data Access and Handling: 1.1 Personal Data: The API accessese, collects, stores, or processes personal data such as names, addresses, email addresses, phone numbers, ID numbers, etc. 1.2 Sensitive Information: The API handles sensitive information such as biometric data (fingerprints, facial recognition), health data, financial information, etc. 1.3 Sensitive Device Permissions: The API collects or handles sensitive device data such as location, contacts, SMS, device identification information (device ID, Android ID, Advertising ID, etc.)
2. Data Transmission and Storage: 2.1 Encryption: The API uses encryption technologies (e.g., HTTPS, encryption libraries) to protect data during transmission and storage 2.2 Data Storage Location: The API specifies where data is stored and ensures compliance with relevant privacy laws and regulations.
3. User Control and Consent: 3.1 User Consent: The API obtains explicit user consent before collecting or processing data, and allow users to withdraw consent at any time. 3.2 Data Access and Deletion: The API provides mechanisms for users to access their data and delete their personal information.
4. Transparency and Policy: 4.1 Privacy Policy: There is a detailed privacy policy associated with the API, explaining how data is collected, used, and shared. 4.2 Data Sharing: The API involves sharing user data with third parties.
5. Data Minimization and Purpose Limitation: 5.1 Data Minimization: The API collects and processes  only the minimum amount of data necessary to achieve its function 5.2 Purpose Limitation: The use of the data is clearly defined, ensuring that it is not used for unauthorized purpose.
6. Privacy Law Compliance: 6.1 Legal Compliance: The API is designed to meet compliance requirements of privacy regulations or laws.
Instructions for Summarizing an API:
1. Do not infer information that is not included in the documentation, but feel free to use your prior knowledge to make the description more precise.
2. Be as detailed as possible: include and output ALL information related to the target API. When summarizing each API, also include any relevant conditions, laws, or external factors mentioned in the surrounding context. The conditions/precondtions of a law or policy should also be regarded as the condtions of its corresponding API. For example, The defination of COPPA in the document "COPPA is a federal law that imposes specific requirements on websites and online service operators to protect the privacy of children under 13" should also be regards as a condtion/effect of COPPA API. 
3. Descriptions of the API might be mentioned in different parts of the documentation, not only in the API section. You need to go throught the whole document to extract every description about the API.Ensure you find all related information. 
4. Follow the JSON format strictly as provided, and refer to the example output. Ensure that the JSON data is properly formatted to allow successful parsing, and avoid including any content beyond the JSON (e.g., do not add "json" at the beginning or "" at the end). Use quotation marks ("") to wrap any object that is invalid in JSON.
5. The annotations after each item indicate what needs to be filled in, but do not include comments in your response. If specific information cannot be extracted from the document, leave the item blank.
6. UI-related APIs are not within the scope of our extraction, such as those that display a dialog.

Summary Format:
{
    "SDK": "",
    "privacy_APIs": [
        {
            "API_name": "", // The name of the target method, which will be used to match the method in the code
            "class_name": "", // If the class name is provided in the documentation, record it; otherwise, leave the field blank. Typically, the class name can be identified in the format 'class_name.API_name' within the document.
            "conditions": [], // The list of conditions/precondtions required to call the API
            "effects": [], // The list of effects and consequences of calling the API
            "parameter_configurations": [ // Summary of all configurable parameters or parameter combinations(Each element in the list represents one possible parameter combination);if no parameters in the API, leave it blank. 
                {
                    "parameter_values": [], // one of the parameter combinations mentioned in the document. If some parameter is not configurable or unknown, mark it "null" in the corresponding index in the list.
                    "conditions": [], // The list of conditions/preconditions for setting parameters to parameter_values
                    "effects": [] // The list of effects or consequences of setting parameters to parameter_values
                }
            ]
        }
    ]
}

Output Example:
{
    "SDK": "AppLovin",
    "privacy_APIs": [
        {
            "API_name": "setIsAgeRestrictedUser",
            "class_name": "AppLovinPrivacySettings",
            "conditions": [
                "required to comply with COPPA"
            ],
            "effects": [
                "indicates whether a user is in an age-restricted category"
            ],
            "parameter_configurations": [
                {
                    "parameter_values": [
                        true, "context"
                    ],
                    "conditions": [
                        "The user is under the age of 16"
                    ],
                    "effects": [
                        "Prohibition on Ads to, and Personal Information from, Children and Apps Exclusively Designed for, or Exclusively Directed to, Children"
                    ]
                },
                {
                    "parameter_values": [
                        false, "context"
                    ],
                    "conditions": [
                        "The user is above the age of 16"
                    ],
                    "effects": [
                        "No prohibition on Ads to, and Personal Information from, Children and Apps Exclusively Designed for, or Exclusively Directed to, Children"
                    ]
                }
            ]
        },
        {
            "API_name": "setDoNotSell",
            "class_name": "AppLovinPrivacySettings",
            "conditions": [
                "required to display a 'Do Not Sell or Share My Personal Information' link to users in those states, or to provide other options through which those users can opt out of interest-based advertising"
            ],
            "effects": [
                "users can opt out of both interest-based advertising and the sale or sharing of their personal information for the purpose of interest-based advertising"
            ],
            "parameter_configurations": [
                {
                    "parameter_values": [
                        true, "context"
                    ],
                    "conditions": [
                        "user opts out of interest-based advertising"
                    ],
                    "effects": [
                        "user opts out of interest-based advertising"
                    ]
                },
                {
                    "parameter_values": [
                        false, "context"
                    ],
                    "conditions": [
                        "user does not opt out of interest-based advertising"
                    ],
                    "effects": [
                        "user does not opt out of interest-based advertising"
                    ]
                }
            ]
        }
    ]
}
"""

def recordResponseAsPlainText(sdk, response):
    with open(f"plaintext_summaries_md2/{sdk}.txt", 'a') as file:
        file.write(response)

def analyze(user_prompt, sdk):

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        response = str(completion.choices[0].message.content)
        recordResponseAsPlainText(sdk, response)
        actual_json_str = json.loads(response)
        beautified_json = json.dumps(actual_json_str, indent=4)
        with open(f"summaries_md2/{sdk}.json", 'a') as file:
            file.write(beautified_json)


    except json.JSONDecodeError as e:
        with open(errorlog_name, 'a') as errorlog:
            errorlog.write(f"SDK:{sdk}, JSONDecodeError: {e} \n")
    except Exception as e:
        with open(errorlog_name, 'a') as errorlog:
            errorlog.write(f"SDK:{sdk}, Error:{e} \n")

def analyzeSDK(SDK):
    message = f"SDK name: {SDK}\nDocumentation:\n"
    file_path = os.path.join(doc_source, SDK)
    for filename in os.listdir(file_path):
        with open(os.path.join(file_path, filename), 'r') as file:
            message += file.read()
    with open(f"messages_md2/{SDK}.md", 'w', encoding='utf-8') as file:
        file.write(message)
    analyze(message, SDK)

doc_source = f"../web_archive/privacy_doc_md_group/"
summary_directory = f"summaries_md2"

with open(errorlog_name, 'a') as errorlog:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    errorlog.write(f"{current_time} ----------------------------- \n")
for directory in os.listdir(doc_source):
    if f"{directory}.json" in os.listdir(summary_directory):
        print(f"has summary: {directory}")
        continue
    print(f"start: {directory}")

    analyzeSDK(directory)













