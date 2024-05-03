import requests
from bs4 import BeautifulSoup
from googlesearch import search
import os
from openai import OpenAI

client = OpenAI(api_key="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")

def get_api_documentation(sdk_name, api_name):
    # sdk_name = "Admost"
    # api_name = "setSubjectToCCPA"
    query = f"{sdk_name} {api_name}"
    # search api document, get top5
    doc_name = f'api_description_{sdk_name}_{api_name}.txt'
    if os.path.exists(doc_name):
        os.remove(doc_name)
    for j in search(query, num_results=5):
        doc_url = j
        response = requests.get(doc_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        has_api = False

        for div in soup.find_all("div"):
            if api_name in div.text:
                has_api = True
                break

        if has_api:
            print(j)
            with open(doc_name, "a") as f:
                for div in soup.find_all("div"):
                    f.write(div.text)



get_api_documentation("Facebook", "setDataProcessingOptions")
# with open("api_description.txt", "r") as f:
#     document = f.read()

# client = OpenAI(
#     # This is the default and can be omitted
#     api_key="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",
# )

# prompt = f'Summarize the {api_name} API of {sdk_name} SDK (description, usage, requirement, condition, influence, any other important information mentioned in the document, etc.):\n {document}'
#
#
# response = client.completions.create(
#     model="gpt-3.5-turbo",
#     prompt=prompt,
#     max_tokens=50
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": prompt,
#         }
#     ],
#     model="gpt-3.5-turbo",
# )

# print(response.choices[0].text.strip())