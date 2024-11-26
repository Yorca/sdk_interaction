import re
import os
import json
from PIL import Image
import pytesseract
import tools
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
import env
llm = ChatOpenAI(model_name="gpt-4o-mini", api_key=os.getenv('OPENAI_API_KEY')) #model_name="gpt-4o-mini",

def extract_step_and_timestamp(filename):
    """
    Extracts the step number and timestamp from the filename.
    """
    match = re.match(r'step-(\d+)-.*-(\d+)\.png', filename)
    if match:
        step = int(match.group(1))
        timestamp = int(match.group(2))
        return step, timestamp
    return None, None

def extract_step_and_timestamp_from_xml(filename):
    """
    Extracts the step number and timestamp from the filename.
    """
    match = re.match(r'step-(\d+)-.*-(\d+)\.xml', filename)
    if match:
        step = int(match.group(1))
        timestamp = int(match.group(2))
        return step, timestamp
    return None, None


def extract_text_from_image(file_path):
    """
    Extracts the main content from the PNG file using OCR.
    """
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return ""


def summarize_content(content):
    """
    summarize the content extracted from the PNG file.
    """
    # Splitting the content to ensure it fits within the model's context length
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 0)
    document = Document(page_content=str(content))
    split_content = text_splitter.split_documents([document])
    summarize_chain = load_summarize_chain(llm, chain_type="stuff")
    summary = summarize_chain.run(split_content)

    return summary

def process_xml_file(file_path):
    """
    Processes a single file to extract the step, timestamp, and summarized content.
    """
    filename = os.path.basename(file_path)
    step, timestamp = extract_step_and_timestamp_from_xml(filename)

    if step is not None and timestamp is not None:
        with open(file_path, "r") as file:
            data = file.read()
        content = tools.xml_to_text(data)

        return {
            "timestamp": timestamp,
            "content": content
        }
    else:
        return None

def process_file(file_path):
    """
    Processes a single file to extract the step, timestamp, and summarized content.
    """
    filename = os.path.basename(file_path)
    step, timestamp = extract_step_and_timestamp(filename)

    if step is not None and timestamp is not None:
        content = extract_text_from_image(file_path)

        summarized_content = summarize_content(content)

        return {
            # "step": step,
            "timestamp": timestamp,
            "content": summarized_content
        }
    else:
        return None

def get_ui_display_summary(pkg_name):
    folder = os.path.join(env.fastbot_log_path, pkg_name, "fastbot_log")
    png_files = [os.path.join(folder, filename) for filename in os.listdir(folder) if filename.endswith(".png")]
    results = []
    for png_file in png_files:
        result = process_file(png_file)
        if result and (len(results) == 0 or result["content"] != results[-1]["content"]): # avoid duplicate
            results.append(result)
    return results

def get_ui_display_summary_with_xml(pkg_name):
    folder = os.path.join(env.fastbot_log_path, pkg_name, pkg_name)
    if not os.path.exists(folder):
        return []
    xml_files = [os.path.join(folder, filename) for filename in os.listdir(folder) if filename.endswith(".xml")]
    results = []
    for xml_file in xml_files:
        result = process_xml_file(xml_file)
        if result and (len(results) == 0 or result["content"] != results[-1]["content"]): # avoid duplicate
            results.append(result)
    return results

def get_click_event_summary(pkg_name):
    file_path = os.path.join(env.click_event_log_path, pkg_name + ".log")
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file:
        log_data = file.read()
    pattern = re.compile(
        r"Found Node Start ---.*?Clicked Node:\s*(.*?)Page XML:\s*(.*?)timestamp:\s*(\d+).*?Found Node End ---",
        re.DOTALL)
    matches = pattern.findall(log_data)

    result = []
    for match in matches:
        clicked_node, page_xml, timestamp = match
        if "[Fastbot]*** WARNING ***" in clicked_node or "[Fastbot]*** WARNING ***" in page_xml:
            continue
        if not clicked_node.strip() or clicked_node.strip() == "null":
            continue
        result.append({
            "timestamp": int(timestamp),
            "click": f"{clicked_node.strip()}",
            "in page": f"{page_xml.strip()}"
        })



    with open(f"res/ui/{pkg_name}.json", "a") as file:
        file.write(json.dumps(result, indent=4))
    return result