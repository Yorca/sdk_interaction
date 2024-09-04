from openai import OpenAI
from bs4 import BeautifulSoup
import os
import json
import email
import email
from html.parser import HTMLParser
from goose3 import Goose

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def read_and_parse_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    text_content = soup.get_text(separator='\n', strip=True)
    return text_content

def read_and_parse_mhtml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        mhtml_content = f.read()
    msg = email.message_from_string(mhtml_content)

    for part in msg.walk():
        if part.get_content_type() == "text/html":
            html_content = part.get_payload(decode=True).decode('utf-8')

    parser = HTMLParser()
    parser.feed(html_content)

    return html_content

sys_prompt = """
You are a Privacy API Summarizer. You will be provided with a document that may contain one or more privacy-related APIs. Your task is to:
1. Identify these APIs within the document.
2. Gather all relevant texts (directly or indirectly related) concerning the identified API(s).
3. Extract and Summarize the information regarding these privacy APIs using the provided format.
Definition of a Privacy API:
An API is considered a privacy API if it is explicitly privacy-related, or if it meets any of the following criteria:
1. Data Access and Handling: 1.1 Personal Data: Does the API access, collect, store, or process personal data such as names, addresses, email addresses, phone numbers, ID numbers, etc.? 1.2 Sensitive Information: Does the API handle sensitive information such as biometric data (fingerprints, facial recognition), health data, financial information, etc.? 1.3 Sensitive Device Permissions: Does the API collect or handle sensitive device data such as location, contacts, SMS, device identification information (device ID, Android ID, Advertising ID, etc.)?
2. Data Transmission and Storage: 2.1 Encryption: Does the API use encryption technologies (e.g., HTTPS, encryption libraries) to protect data during transmission and storage? 2.2 Data Storage Location: Does the API specify where data is stored and ensure compliance with relevant privacy laws and regulations?
3. User Control and Consent: 3.1 User Consent: Does the API obtain explicit user consent before collecting or processing data, and allow users to withdraw consent at any time? 3.2 Data Access and Deletion: Does the API provide mechanisms for users to access their data and delete their personal information?
4. Transparency and Policy: 4.1 Privacy Policy: Is there a detailed privacy policy associated with the API, explaining how data is collected, used, and shared? 4.2 Data Sharing: Does the API involve sharing user data with third parties, and are users clearly informed about this sharing?
5. Data Minimization and Purpose Limitation: 5.1 Data Minimization: Does the API collect and process only the minimum amount of data necessary to achieve its function? 5.2 Purpose Limitation: Is the use of the data clearly defined, ensuring that it is not used for unauthorized purposes?
6. Privacy Law Compliance: 6.1 Legal Compliance: Is the API designed to meet compliance requirements of privacy regulations or laws?
Instructions for Summarizing an API:
1. Do not infer information that is not included in the documentation, but feel free to use your prior knowledge to make the description more precise.
2. Include all significant details related to the target API.
3. Reference all relevant sections: Descriptions of the API might be mentioned in different parts of the documentation, not only in the API section. Ensure you find all related information.
4. Strictly follow the JSON format provided below. The annotations after each item indicate what should be filled in. If you cannot extract the corresponding information from the document, leave the item blank.

Summary Format:
{
    "SDK": "",
    "privacy_APIs": [
        {
            "API_name": "", // The name of the target API
            "conditions": [], // The list of conditions required to call the API
            "effects": [], // The list of effects and consequences of calling the API
            "parameter_configurations": [ // Summary of all configurable parameters or parameter combinations; if no parameters in the API, leave it blank.
                {
                    "parameter_values": [], // One of the parameter combinations mentioned in the document. If some parameter is not configurable or unknown, mark it "null" in the corresponding index in the list.
                    "conditions": [], // The list of conditions or requirements for setting parameters to parameter_values
                    "effects": [] // The list of effects or consequences of setting parameters to parameter_values
                }
            ]
        }
    ]
}

Summary Example:
{
    "SDK": "AppLovin",
    "privacy_APIs": [
        {
            "API_name": "setIsAgeRestrictedUser",
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
            "conditions": [
                "required to display a 'Do Not Sell or Share My Personal Information' link to users in those states, or to provide other options through which those users can opt out of interest-based advertising"
            ],
            "effects": [
                "users can opt out of both interest-based advertising and the sale or sharing of their personal information for the purpose of interest-based advertising"
            ],
            "parameter_configurations": [
                {
                    "parameter_values": [
                        true, context
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
                        false, context
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

def analyze(user_prompt, sdk):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        print(str(completion.choices[0].message.content))
        actual_json_str = json.loads(str(completion.choices[0].message.content))
        print(actual_json_str)
        beautified_json = json.dumps(actual_json_str, indent=4)
        with open(f"summaries/{sdk}.json", 'a') as file:
            file.write(beautified_json)
    except json.JSONDecodeError as e:
        with open("error_log.txt", 'a') as errorlog:
            errorlog.write(f"SDK:{sdk}, JSONDecodeError: {e} \n")
    except Exception as e:
        with open(f"error_log", 'a') as errorlog:
            errorlog.write(f"SDK:{sdk}, Error:{e} \n")



# def has_analyzed(sdk, api):
#     folder = "responses"
#     for root, dirs, files in os.walk(folder):
#         for file in files:
#             if sdk in file and api in file:
#                 return True
#     return False

doc_source = "../web_archive/privacy_docs_group/"
def analyzeSDK(SDK):
    message = f"SDK name: {SDK}\nDocumentation:\n"
    file_path = os.path.join(doc_source, SDK)
    for filename in os.listdir(file_path):
        if filename.endswith(".html"):
            message += read_and_parse_html(os.path.join(file_path, filename))
        elif filename.endswith(".mhtml"):
            message += read_and_parse_mhtml(os.path.join(file_path, filename))
    # message = message[:int(len(message) * 0.85)]
    analyze(message, SDK)

#print(json.loads('{\n    "SDK": "Splunk MINT",\n    "privacy_APIs": [\n        {\n            "API_name": "transactionStart",\n            "conditions": [\n                "Used when a transaction begins"\n            ],\n            "effects": [\n                "Starts a transaction. Returns a transaction ID"\n            ],\n            "parameter_configurations": [\n                {\n                    "parameter_values": [\n                        "name"\n                    ],\n                    "conditions": [\n                        "Transaction name is provided"\n                    ],\n                   '))


for directory in os.listdir(doc_source):
    analyzeSDK(directory)













