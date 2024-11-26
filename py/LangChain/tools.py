from langchain.tools import Tool
import json
import env

import xml.etree.ElementTree as ET
import re
import nltk
from nltk.corpus import stopwords, words
from nltk.tokenize import word_tokenize
import xml.etree.ElementTree as ET


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('words')

summary_ground_truth = env.summary_ground_truth

def xml_to_text(xml_content):
    # Parse XML
    root = ET.fromstring(xml_content)

    def extract_text(node, level=0):
        # Indentation for readability based on level of depth
        indentation = ' ' * level

        # Get the text content of the node if available
        text_content = node.get('text')

        # Only include nodes that have non-empty text fields
        result = ""
        if text_content:
            result += f"{indentation}{text_content}\n"

        # Process child nodes recursively
        for child in node:
            result += extract_text(child, level + 1)

        return result

    # Generate and return the structured text with only 'text' fields
    return extract_text(root)

def xml_to_text(xml_content):
    # Parse XML
    root = ET.fromstring(xml_content)

    def extract_text(node, level=0):
        # Indentation for readability based on level of depth
        indentation = ' ' * (level * 4)

        # Get the text content of the node if available
        text_content = node.get('text')

        # Only include nodes that have non-empty text fields
        result = ""
        if text_content:
            result += f"{indentation}{text_content}\n"

        # Process child nodes recursively
        for child in node:
            result += extract_text(child, level + 1)

        return result

    # Generate and return the structured text with only 'text' fields
    return extract_text(root)

import re
from nltk.corpus import words

english_words = set(words.words())

def camel_case_to_words(method_name):
    if len(method_name) <= 2:
        return None
    words_list = re.findall(r'[A-Za-z][a-z]*|[A-Z][a-z]*', method_name)
    if all(word.lower() in english_words for word in words_list):
        return ' '.join(words_list)
    else:
        return None


def is_obfuscated(method_name):
    print("start is_obfuscated")
    english_words = set(words.words())
    method_name = method_name.lower()
    if method_name in english_words:
        return False
    vowels = set('aeiou')
    num_vowels = sum(1 for char in method_name if char in vowels)
    if len(method_name) == 0:
        return True
    vowel_ratio = num_vowels / len(method_name)
    if vowel_ratio < 0.3:
        return True
    if not any(char in vowels for char in method_name):
        return True
    return False

def get_purpose_of_sensitive_api(cls, mtd):
    with open("../Dynamic/data/sensitive_apis.json", "r") as file:
        data = json.load(file)

    for api in data:
        if api['class'] == cls and api['method'] == mtd:
            return api["action"]
    return None

def get_summary(class_name, mtd_name):
    with open(summary_ground_truth, "r") as file:
        data = json.loads(file.read())
    for sdk in data["LIBS"]:
        for api in sdk["privacy_APIs"]:
            for cls in api["class_name"]:
                if cls == class_name and (not mtd_name or mtd_name == api['API_name']):
                    del api["API_name"]
                    del api["class_name"]
                    return api
    return None
