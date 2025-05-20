from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from pathlib import Path

CHROMA_DIR = "chroma_store"

def load_and_embed_terraform(folder_path="infra"):
    docs = []
    for file in Path(folder_path).rglob("*.tf"):
        loader = TextLoader(str(file))
        docs.extend(loader.load())

    if not docs:
        print("⚠️ No Terraform documents found to embed.")
        return

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    print(f"📄 Loaded {len(chunks)} document chunks from Terraform files.")

    vectorstore = Chroma.from_documents(
        chunks,
        embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
        persist_directory=CHROMA_DIR
    )
    vectorstore.persist()
    print("✅ Embedding complete.")
    return vectorstore


# ✅ New function for LangGraph agent
def load_code_context(folder_path="infra", top_k=5):
    """
    Load top-k most relevant chunks from ChromaDB without a question.
    This simulates "summary context" for prompt injection.
    """
    vectorstore = Chroma(
        embedding_function=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
        persist_directory=CHROMA_DIR
    )
    # Fallback dummy query to retrieve high-salience chunks
    docs = vectorstore.similarity_search("infrastructure overview", k=top_k)
    return "\n\n".join([doc.page_content for doc in docs])
