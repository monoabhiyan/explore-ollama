from config import DOCS_DIR
from db.vector_store import collection
from pipeline.document_processor import process_and_add_documents
from rag import rag_query

# print("Indexing....")
# process_and_add_documents(collection, DOCS_DIR)

query = "How many years of exp Abhiyan have and what are his skills, how many years Abhiyan have worked on  ?"
response, sources = rag_query(collection, query)

# Print results
print("\nQuery:", query)
print("\nAnswer:", response)
print("\nSources used:")
for source in sources:
    print(f"- {source}")

