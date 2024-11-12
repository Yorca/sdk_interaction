
import json
import os.path

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import tools
from loaders import load_api_trace, load_api_summary, load_ui_trace, load_app_property, load_web
from langchain.text_splitter import RecursiveCharacterTextSplitter
import env
from ui_trace_generator import get_ui_display_summary, get_click_event_summary
from langchain_community.document_loaders import TextLoader, UnstructuredXMLLoader, UnstructuredImageLoader, JSONLoader, WebBaseLoader
import xml.etree.ElementTree as ET
import json
embedding_model = OpenAIEmbeddings()
def get_api_trace(pkg_name):
    path = os.path.join(env.apk_log_folder, pkg_name + ".log")
    if not os.path.exists(path):
        return None, False, False
    with open(path) as file:
        data = "[" + file.read()[:-2] + "]"
    data = json.loads(data)
    fields_to_keep = {"method", "class_name", "timestamp", "arguments", "is_privacy", "return", "source"}
    filtered_data = [{k: v for k, v in item.items() if k in fields_to_keep} for item in data]

    has_privacy_api = False
    has_sensitive_api = False

    for trace in filtered_data:
        if trace["is_privacy"]:
            has_privacy_api = True
        if trace["source"] == "sensitive":
            has_sensitive_api = True
    print(filtered_data)




    return filtered_data, has_privacy_api, has_sensitive_api

def get_app_property(pkg_name, fields):
    with open(os.path.join(env.app_detail_path, pkg_name), "r") as file:
        data = file.read()
    data = json.loads(data)
    if fields:
        data = {k: v for k, v in data.items() if k in fields}
    return data


def add_event_type(trace, event_type):
    for item in trace:
        item["event_type"] = event_type

def get_summaries(trace):
    added_list = []
    sums = []
    for item in trace:
        cls = item['class_name']
        mtd = item['method']
        sig = f"{cls};{mtd}"
        if sig in added_list:
            continue
        added_list.append(sig)
        print(cls)
        print(mtd)
        sums.append(tools.get_summary(cls, mtd))
    return sums


def load_summary(trace):
    for item in trace:
        cls = item['class_name']
        mtd = item['method']
        item["api_summary"] = tools.get_summary(cls, mtd)

def get_summaries_V2(trace):
    added_list = []
    sums = []
    for item in trace:
        cls = item['class_name']
        sig = cls
        if sig in added_list:
            continue
        added_list.append(sig)
        print(cls)
        sums.append(tools.get_summary(cls, None))
    return sums


def extract_text_and_content_desc(xml_string):
    # Parse the XML string
    root = ET.fromstring(xml_string)
    # List to store extracted text and content-desc values
    extracted_values = []
    # Recursive function to iterate through nodes
    def extract_recursive(node):
        # Get the 'text' and 'content-desc' attributes
        text = node.get("text", "").strip()
        content_desc = node.get("content-desc", "").strip()
        # Add to the list if text or content-desc has a non-empty value
        if text:
            extracted_values.append(f"text: {text}")
        if content_desc:
            extracted_values.append(f"content-desc: {content_desc}")
        # Recur for child nodes
        for child in node:
            extract_recursive(child)
    # Start recursive extraction from root node
    extract_recursive(root)
    return extracted_values

def summarize_click(trace):
    if not trace or not "click" in trace.keys():
        return None

    if trace["click"] == "null":
        return None

    click = extract_text_and_content_desc(trace["click"])
    page_content = extract_text_and_content_desc(trace["in"])

    return f"click: {click} in page: {page_content}"

def parse_xml_trace(trace):
    new_trace = []
    for item in trace:
        new_trace.append({
            "timestamp": item["timestamp"],
            "event": summarize_click(item)
        })
    return new_trace


def get_trace(pkg):
    api_trace, has_privacy_api, has_sensitive_api = get_api_trace(pkg)
    print(api_trace)
    if not api_trace or not has_privacy_api:
        return None
    load_summary(api_trace)
    add_event_type(api_trace, "method call")
    ui_display_trace = get_ui_display_summary(pkg)
    add_event_type(ui_display_trace, "UI Display")
    click_trace = parse_xml_trace(get_click_event_summary(pkg))

    add_event_type(click_trace, "View Click")
    traces = sorted(api_trace + ui_display_trace + click_trace, key=lambda x: x['timestamp'])
    data = json.dumps(traces, indent=4)
    with open(f"res/trace/{pkg}.json", "a") as file:
        file.write(data)
    return traces