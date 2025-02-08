import os
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Define paths
DATA_PATH = "data/rawtext.txt"
VECTOR_STORE_PATH = "vector_store/faiss_index"

# Ensure folders exist
os.makedirs("data", exist_ok=True)
os.makedirs("vector_store", exist_ok=True)

# Check if raw text is already extracted
if not os.path.exists(DATA_PATH):
    print("Extracting data from URL...")
    url = "https://brainlox.com/courses/category/technical"

    # Using UnstructuredURLLoader instead of WebBaseLoader
    loader = UnstructuredURLLoader(urls=[url])
    docs = loader.load()

    # Save extracted text for future use
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        for doc in docs:
            f.write(doc.page_content + "\n")
else:
    print("Using cached data from rawtext.txt")
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        docs = [doc.strip() for doc in f.readlines()]

# Generate embeddings
print("Generating embeddings and saving FAISS index...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_db = FAISS.from_texts(docs, embeddings)

# Save vector store
vector_db.save_local(VECTOR_STORE_PATH)
print("FAISS index saved successfully!")
