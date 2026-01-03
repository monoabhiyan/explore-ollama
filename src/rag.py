from db.retriever import get_context_with_sources, semantic_search
from llm.ollama import generate_response


def rag_query(collection, query: str, n_chunks: int = 2):
    """Perform RAG query: retrieve relevant chunks and generate answer"""

    results = semantic_search(collection, query, n_chunks)
    context, sources = get_context_with_sources(results)

    response = generate_response(query, context)

    return response, sources
