
import json
import os.path

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import tools
from loaders import load_api_trace, load_api_summary, load_ui_trace, load_app_property, load_web
from langchain.text_splitter import RecursiveCharacterTextSplitter
import env
from ui_trace_generator import get_ui_display_summary, get_click_event_summary, get_ui_display_summary_with_xml
from langchain_community.document_loaders import TextLoader, UnstructuredXMLLoader, UnstructuredImageLoader, JSONLoader, WebBaseLoader
import xml.etree.ElementTree as ET
import json
embedding_model = OpenAIEmbeddings()

from collections import deque

def is_directly_related(a, b):

    set_a, set_b = set(a), set(b)
    return set_a.issubset(set_b) or set_b.issubset(set_a)

def build_graph(arr_of_lists):
    n = len(arr_of_lists)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if is_directly_related(arr_of_lists[i], arr_of_lists[j]):
                adj[i].append(j)
                adj[j].append(i)
    return adj

def find_index_of_p(arr_of_lists, p):
    set_p = set(p)
    for i, item in enumerate(arr_of_lists):
        if set(item) == set_p and len(item) == len(p):
            return i
    return -1

def bfs_connected_components(adj, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        cur = queue.popleft()
        for nxt in adj[cur]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return visited

def find_all_related(arr_of_lists, p):

    start_idx = find_index_of_p(arr_of_lists, p)
    if start_idx == -1:
        return []
    adj = build_graph(arr_of_lists)

    related_indices = bfs_connected_components(adj, start_idx)

    return [arr_of_lists[i] for i in related_indices]

def is_test_method(mtd):
    words = ['debug', "Debug", "test", "Test", "getInstance"]
    for word in words:
        if word in mtd:
            return True
    return False

def add_prefix(trace):
    if not trace:
        return None
    prefixes = []
    with open("../Dynamic/data/apis_v2.json", "r") as file:
        classes = json.loads(file.read())
    class_prefixes = ['.'.join(cls["Class"].split('.')[:2]) for cls in classes]
    class_prefixes = list(set(class_prefixes))
    for api in trace:
        stack_trace = api['stack_trace']
        lines = []
        for line in stack_trace.split('\n\tat'):
            trimmed_line = line.strip()
            if trimmed_line and any(trimmed_line.startswith(prefix) for prefix in class_prefixes):
                splits = trimmed_line.split('.')
                pre = splits[:min(2, len(splits))]
                pre = '.'.join(pre)
                if pre not in lines:
                    lines.append(pre)
        # prefix = list(set(lines))
        # prefix = [pre for pre in prefix if not pre.startswith('java.') and not pre.startswith('com.android.') and not pre.startswith('android.')]
        api['prefix'] = lines
        if api["is_privacy"]:
            prefixes.append(lines)
    return prefixes

def get_connected_prefix(prefixes, trace):
    # print(f"prefixes = {prefixes}")
    # print(f"trace = {trace}")
    if not trace:
        return None
    effective_prefix = []
    for api in trace:
        if "is_privacy" in api.keys() and api['is_privacy']:
            con_prefixes = find_all_related(prefixes, api['prefix'])
            if not con_prefixes:
                continue
            print(f"con_prefixes = {con_prefixes}")
            api['connected_prefix'] = con_prefixes
            con_prefixes.append(api['prefix'])
            for new_pre in con_prefixes:
                if new_pre not in effective_prefix:
                    effective_prefix.append(new_pre)
            # effective_prefix += con_prefixes
            # .append(api['prefix'])

    return effective_prefix

def is_effective_prefix(prefix, pri_prefixes):
    for pri_pre in pri_prefixes:
        pre_str = ';'.join(prefix)
        pri_str = ';'.join(pri_pre)
        if pre_str in pri_str or pri_str in pre_str:
            return True
        # if set(pri_pre).issubset(set(prefix)) or set(prefix).issubset(set(pri_pre)):
        #     return True
    return False
            


def get_api_trace(pkg_name):
    path = os.path.join(env.apk_log_folder, pkg_name + ".log")
    if not os.path.exists(path):
        return None, False, False
    with open(path) as file:
        data = "[" + file.read()[:-2] + "]"
        if not '"is_privacy": true' in data:
            return None, False, False
    data = json.loads(data)
    fields_to_keep = {"method", "class_name", "timestamp", "arguments", "is_privacy", "return", "source", "stack_trace"}
    filtered_data = [{k: v for k, v in item.items() if k in fields_to_keep} for item in data]
    all_prefix = add_prefix(filtered_data)
    print(f"effective_prefix = {all_prefix}")
    has_privacy_api = False
    has_sensitive_api = False
    new_trace = []
    meaningful_mtds = set()
    meaningless_mtds = set()
    count = 0

    for trace in filtered_data:
        if not is_effective_prefix(trace['prefix'], all_prefix):
            count += 1
            with open(f"res/removed_trace/{pkg_name}.log", "a") as file:
                file.write(json.dumps(f"{trace}", indent=4) + '\n\n')
            continue

        if tools.isPricacyAPI(trace['class_name'], trace['method']):
            has_privacy_api = True
            new_trace.append(trace)
        elif trace["source"] == "sensitive":
            action = tools.get_purpose_of_sensitive_api(trace["class_name"], trace["method"])
            if not action:
                continue
            trace["action"] = action
            has_sensitive_api = True
            new_trace.append(trace)
        elif trace["method"] in meaningless_mtds:
            continue
        elif trace["method"] in meaningful_mtds or (not is_test_method(trace["method"]) and tools.camel_case_to_words(trace["method"])):
            meaningful_mtds.add(trace["method"])
            new_trace.append(trace)
        else:
            meaningless_mtds.add(trace["method"])
    with open("stat.txt", "a") as file:
        file.write(f"remove {count}/{len(filtered_data)}\n")
    print(f"remove {count}/{len(filtered_data)}")

    return new_trace, has_privacy_api, has_sensitive_api

def get_app_property(pkg_name, fields):
    with open(os.path.join(env.app_detail_path, pkg_name), "r") as file:
        data = file.read()
    data = json.loads(data)
    if fields:
        data = {k: v for k, v in data.items() if k in fields}
    return data


def add_event_type(trace, event_type):
    if not trace:
        return
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

    if not trace["click"] or trace["click"] == "null":
        return None
    click = tools.xml_to_text(trace["click"])
    if not click:
        return None
    page_content = tools.xml_to_text(trace["in page"])

    return f"click: [{click}] in page: [{page_content}]"

def parse_xml_trace(trace):
    new_trace = []
    for item in trace:
        sum = summarize_click(item)
        print(sum)
        if not sum:
            continue
        new_trace.append({
            "timestamp": item["timestamp"],
            "event": sum
        })
    print(f"new_trace {new_trace}")
    return new_trace


def get_trace(pkg):
    api_trace, has_privacy_api, has_sensitive_api = get_api_trace(pkg)
    if not api_trace or not has_privacy_api:
        return None
    load_summary(api_trace)
    add_event_type(api_trace, "method call")
    # ui_display_trace = get_ui_display_summary_with_xml(pkg)
    # add_event_type(ui_display_trace, "UI Display")
    click_trace = parse_xml_trace(get_click_event_summary(pkg))
    add_event_type(click_trace, "View Click")


    # traces = sorted(api_trace + ui_display_trace + click_trace, key=lambda x: x['timestamp'])
    traces = sorted(api_trace + click_trace, key=lambda x: x['timestamp'])
    if pkg == 'com.cider':
        print(f"traces = {traces}")
    data = json.dumps(traces, indent=4)
    with open(f"res/trace/{pkg}.json", "a") as file:
        file.write(data)
    return traces
