
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import tools
from agent import get_agent
from loaders import load_api_trace, load_api_summary, load_ui_trace, load_app_property, load_web
from langchain.text_splitter import RecursiveCharacterTextSplitter
import env
embedding_model = OpenAIEmbeddings()

pkg_list = []
for pkg in pkg_list:
    api_trace_docs = load_api_trace(pkg)
    xml_docs, img_docs = load_ui_trace(pkg)
    summary_docs = load_api_summary()
    api_property_docs = load_app_property(pkg)
    runtime_env = env.runtime_environment
    datasafety_docs = load_web(f"https://play.google.com/store/apps/datasafety?id={pkg}&hl=en&gl=us")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=0
    )
    detector = get_agent()
    template = f"""
    Please detect privacy API inconsistency based on the follow information:
    
    % API trace documents
    {text_splitter.split_text(api_property_docs)}
    
    % UI trace documents
    {text_splitter.split_text(xml_docs + img_docs)}
    
    % summary documents
    {text_splitter.split_text(summary_docs)}
    
    % api property documents
    {text_splitter.split_text(api_property_docs)}
    
    % app data safety documents
    {text_splitter.split_text(datasafety_docs)}

    % runtime environment
    {runtime_env}
    
    """
    detector.run("")

    

    







