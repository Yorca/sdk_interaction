import re
import os
import json
from PIL import Image
import pytesseract
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
import env
llm = OpenAI(api_key=os.getenv('OPENAI_API_KEY')) #model_name="gpt-4o-mini",

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


def extract_text_from_image(file_path):
    """
    Extracts the main content from the PNG file using OCR.
    """
    try:
        # loader = UnstructuredImageLoader(file_path)
        # return loader.load()
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
    print(len(split_content))
    # Create a summarization chain
    summarize_chain = load_summarize_chain(llm, chain_type="stuff")
    # , prompt = """"
    #         Please summarize the content field, and output in original format:
    #         [{
    #             "step": step,
    #             "timestamp": timestamp,
    #             "content": content
    #         }]
    #     """
    summary = summarize_chain.run(split_content)

    return summary


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
    folder = os.path.join(env.fastbot_log_path, pkg_name)
    png_files = [os.path.join(folder, filename) for filename in os.listdir(folder) if filename.endswith(".png")]
    results = []
    print(png_files)
    for png_file in png_files:
        result = process_file(png_file) # TODO: add prompt to make the summary more accurate
        if result:
            results.append(result)
    return results
def get_click_event_summary(pkg_name):
    file_path = os.path.join(env.click_event_log_path, pkg_name)
    with open(file_path, "r") as file:
        data = json.loads(file.read())
    return data