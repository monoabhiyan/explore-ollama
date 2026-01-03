from config import DOCS_DIR
from db.vector_store import collection
from pipeline.document_processor import process_and_add_documents
from rag import rag_query

print("Indexing....")
process_and_add_documents(collection, DOCS_DIR)


query = "1. abhiyan and nikesh work exp ?"

print('Answering...')
response, sources = rag_query(collection, query, n_chunks=5)

# Print results
print("\nQuery:", query)
print("\nAnswer:", response)
print("\nSources used:")
for source in sources:
    print(f"- {source}")

