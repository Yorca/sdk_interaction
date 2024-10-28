from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI
from langchain.document_loaders import DirectoryLoader, JSONLoader
from langchain.chains import RetrievalQA

loader = JSONLoader('data/api_summary_groundtruth.json', jq_schema=".LIBS[]", text_content=False)
documents = loader.load()
print(documents)

text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
split_docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
docsearch = Chroma.from_documents(split_docs, embeddings)

qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever(), return_source_documents=True)
with open("log/priv_log/com.hiface.log_new.log", "r") as file:
    log_detail = "[" + file.read()[:-1] + "]"
result = qa({"query": f"Find the privacy APIs in the log:\n {log_detail[:int(len(log_detail) / 4)]}"})
print(result)