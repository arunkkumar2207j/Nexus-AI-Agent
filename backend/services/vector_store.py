import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Initialize Embeddings (Free, Local)
# using a lightweight model for speed
embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

PERSIST_DIRECTORY = "./chroma_db"

def get_vector_store():
    return Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embedding_function
    )

def ingest_document(file_path: str):
    """Loads a PDF, splits it, and saves to vector store."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    loader = PyPDFLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(docs)

    vectorstore = get_vector_store()
    vectorstore.add_documents(documents=splits)
    
    return len(splits)

def get_retriever():
    vectorstore = get_vector_store()
    return vectorstore.as_retriever()
