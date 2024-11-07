import re
import os
import json
from PIL import Image
import pytesseract
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain_community.document_loaders import TextLoader, UnstructuredXMLLoader, UnstructuredImageLoader, JSONLoader, WebBaseLoader

# Initialize OpenAI LLM (ensure to replace 'your-openai-api-key' with your key)
llm = OpenAI(api_key=os.getenv('OPENAI_API_KEY')) #model_name="gpt-4o-mini",


# Set path to your Tesseract executable if it's not in your PATH
# For example, on Windows:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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
    # step, timestamp = extract_step_and_timestamp(filename)
    content = extract_text_from_image(file_path)

    summarized_content = summarize_content(content)

    return {
        "content": summarized_content
    }



# Example usage
png_files = ["/Users/yorca/Downloads/socksrevive.plugin.dragon.png"]  # Add paths to your PNG files

results = []
for png_file in png_files:
    result = process_file(png_file)
    if result:
        results.append(result)

# Output the results as JSON
print(json.dumps(results, indent=4))
