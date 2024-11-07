import json
import os.path

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import tools
from agent import get_agent
from loaders import load_api_trace, load_api_summary, load_ui_trace, load_app_property, load_web
from langchain.text_splitter import RecursiveCharacterTextSplitter
import env
from ui_trace_generator import get_ui_display_summary, get_click_event_summary
from chains import get_chain

embedding_model = OpenAIEmbeddings()
def get_api_trace(pkg_name):
    with open(os.path.join(env.apk_log_folder, pkg_name + ".log")) as file:
        data = "[" + file.read()[:-2] + "]"
    data = json.loads(data)
    fields_to_keep = {"method", "class_name", "timestamp", "ref", "arguments", "stack_trace", "is_privacy"}
    filtered_data = [{k: v for k, v in item.items() if k in fields_to_keep} for item in data]

    return filtered_data

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
        sig = f"{cls};{mtd}"
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
#
# print(tools.get_summary("com.fyber.inneractive.sdk.external.InneractiveAdManager", "setGdprConsent"))
#
pkg_list = ["com.sdkint.applovinfacebook4"]
for pkg in pkg_list:
    test_pkg = "com.whatsapp"
    api_trace = get_api_trace(pkg)
    # summaries = get_summaries(api_trace)
    load_summary(api_trace)
    add_event_type(api_trace, "method call")
    ui_display_trace = get_ui_display_summary(pkg)[:3]
    add_event_type(ui_display_trace, "UI Display")
    click_trace = get_click_event_summary(pkg)
    add_event_type(click_trace, "View Click")
    traces = sorted(api_trace + ui_display_trace + click_trace, key=lambda x: x['timestamp'])
    data = json.dumps(traces, indent=4)
    with open("traces5.json", "a") as file:
        file.write(data)
    # print(f"trace: {str(traces)}")
    # app_property = get_app_property(test_pkg, ["title", "description", "summary", "contentRating", "contentRatingDescription", "adSupported", "containsAds"]) # TODO: should we also load privacy policy?
    # datasafety_info = load_web(f"https://play.google.com/store/apps/datasafety?id={test_pkg}&hl=en&gl=us")
    # print(datasafety_info)
    # app_property["data safety"] = "\n".join([doc.page_content for doc in datasafety_info])
    # detect_chain = get_chain()
    #
    # inputs = {
    #     "app_details": app_property,
    #     "runtime_environment": env.runtime_environment,
    #     "runtime_traces": traces,
    #     "summaries": summaries
    # }
    #
    # # Run the chain with the defined input
    # output = detect_chain.run(inputs)
    # with open(f"res/{pkg}.txt", "a") as file:
    #     file.write(output)
    # # print(output)











