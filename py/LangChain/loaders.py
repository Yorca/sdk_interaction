import json
import os
import re
from langchain_community.document_loaders import TextLoader, UnstructuredXMLLoader, UnstructuredImageLoader, JSONLoader, WebBaseLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import tools
from agent import get_agent
import env
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

apk_log_folder = env.apk_log_folder
fastbot_log_path = env.fastbot_log_path
app_detail_path = env.app_detail_path
embedding_model = OpenAIEmbeddings()


def add_description(docs, description):
    for doc in docs:
        doc.metadata["description"] = description
    return docs

def load_api_trace(pkg):
    log_path = os.path.join(apk_log_folder, f"{pkg}.log")
    api_trace_loader = TextLoader(log_path)
    api_trace_docs = api_trace_loader.load()
    api_trace_docs = add_description(api_trace_docs, "This is the API trace information at runtime")
    return api_trace_docs

def load_xml(path):
    xml_loader = UnstructuredXMLLoader(path)
    xml_docs = xml_loader.load()
    return xml_docs

def load_picture(path):
    img_loader = UnstructuredImageLoader(path)
    img_docs = img_loader.load()
    return img_docs

def extract_n(file_name):
    match = re.search(r'step-(\d+)-', file_name)
    return int(match.group(1)) if match else 0

def load_ui_trace(pkg_name):
    xml_docs = []
    img_docs = []
    for folder in os.listdir(fastbot_log_path):
        if not folder == pkg_name:
            continue
        folder_path = os.path.join(fastbot_log_path, folder)
        file_names = sorted(os.listdir(folder_path), key=extract_n)
        for filename in file_names:
            if filename.endswith('.png') or filename.endswith('.xml'):
                file_info = filename[:-4].split("-")
                if len(file_info) == 5 and file_info[0] == "step":
                    file_path = os.path.join(folder_path, filename)
                    step = int(file_info[1])
                    timestamp = int(file_info[4])
                    docs = load_picture(file_path) if filename.endswith(".png") else load_xml(file_path)
                    for doc in docs:
                        doc.metadata["event_step"] = step
                        doc.metadata["event_timestamp"] = timestamp
                    if filename.endswith('.png'):
                        img_docs += docs
                    else:
                        xml_docs += docs
    return xml_docs, img_docs

def load_app_property(pkg_name):
    for filename in os.listdir(app_detail_path):
        if not filename == pkg_name:
            continue
        js_loader = JSONLoader(os.path.join(app_detail_path, filename))
        js_docs = js_loader.load()
        return js_docs
    return None

def load_api_summary():
    summary_loader = JSONLoader(env.summary_ground_truth)
    summary = summary_loader.load()
    return summary

def load_web(url):
    loader = WebBaseLoader(url)
    docs = loader.load()
    return docs

