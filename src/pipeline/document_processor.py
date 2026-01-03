import os
from utils.file_helper import read_document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def process_document(file_path: str):
    """Process a single document and prepare for ChromaDB"""
    try:
        content = read_document(file_path)

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=700,
            chunk_overlap=150,
        )
        chunks = splitter.split_text(content)

        file_name = os.path.basename(file_path)

        metadatas = [{"source": file_name, "chunk": i} for i in range(len(chunks))]

        ids = [f"{file_name}_chunk_{i}" for i in range(len(chunks))]

        return ids, chunks, metadatas
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return [], [], []


def add_to_collection(collection, ids, texts, metadatas):
    """Add documents to collection in batches"""
    if not texts:
        return

    batch_size = 100
    for i in range(0, len(texts), batch_size):
        end_idx = min(i + batch_size, len(texts))
        collection.add(
            documents=texts[i:end_idx],
            metadatas=metadatas[i:end_idx],
            ids=ids[i:end_idx],
        )


def process_and_add_documents(collection, folder_path: str):
    """Process all documents in a folder and add to collection"""
    files = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, file))
    ]

    for file_path in files:
        print(f"Processing {os.path.basename(file_path)}...")
        ids, texts, metadatas = process_document(file_path)
        add_to_collection(collection, ids, texts, metadatas)
        print(f"Added {len(texts)} chunks to collection")
