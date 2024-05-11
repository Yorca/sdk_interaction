from androguard.misc import AnalyzeAPK
import json
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import os
import time
apk_path = "/Users/yorca/Downloads/Braindom_BrainGamesTest_2.3.2_Apkpure.apk"
keywords = ["gdpr", "ccpa", "consent", "coppa", "agerestrict", "usprivacy", "child"]

def robust_search(query, num_results, delay=5, retries=3):
    while retries > 0:
        try:
            results = search(query, num_results=num_results)
            return results
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                print("Rate limit exceeded. Retrying after delay...")
                time.sleep(delay)  # Wait for 'delay' seconds before retrying
                retries -= 1
                continue
            else:
                return []
    return []

def get_api_documentation(sdk_name, api_name):
    query = f'"{sdk_name}" "{api_name}"'
    print(query)
    doc_name = f'web_docs/{sdk_name}_{api_name}.txt'
    if os.path.exists(doc_name):
        os.remove(doc_name)
    for j in robust_search(query, 3):
        doc_url = j
        print(doc_url)
        response = requests.get(doc_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        has_api = False

        for div in soup.find_all("div"):
            if api_name in div.text:
                has_api = True
                break

        if has_api:
            with open(doc_name, "a") as f:
                for div in soup.find_all("div"):
                    f.write(div.text)
            with open(f"webs/{sdk_name}_{api_name}_{doc_url}.html", "w", encoding="utf-8") as file:
                file.write(response.text)


def find_methods_with_keywords(apk_path, keywords):
    a, d, dx = AnalyzeAPK(apk_path)

    # Store methods containing keywords
    methods_with_keywords = []

    for class_analysis in dx.get_classes():
        for method_analysis in class_analysis.get_methods():
            method = method_analysis.get_method()
            mtd_name = method.name
            if any(keyword in mtd_name for keyword in keywords):
                class_name, descriptor = method.class_name, method.descriptor
                class_name = class_name.lstrip('L').rstrip(';').replace('/', '.')

                methods_with_keywords.append({
                    "class" : class_name,
                    "method_name": mtd_name,
                    "descriptor": descriptor
                })

    return methods_with_keywords



methods = find_methods_with_keywords(apk_path, keywords)
print(methods)
with open("keyword_apis.json", 'w') as file:
    json.dump(methods, file, indent=4)
for mtd in methods:
    cls_name = mtd['class']
    mtd_name = mtd['method_name']
    sdk_name = cls_name.split('.')[1] #infer
    get_api_documentation(sdk_name, mtd_name)


# for method in methods:
#     print(method)