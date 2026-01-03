import chromadb
from chromadb.utils import embedding_functions

# Initialize ChromeDB client with persisten
client = chromadb.PersistentClient(path="chroma_db")

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.get_or_create_collection(
    name="document_collection", embedding_function=sentence_transformer_ef
)
