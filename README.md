# RAG with Ollama

A simple RAG (Retrieval-Augmented Generation) system using Ollama and ChromaDB.

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Make sure Ollama is running
ollama serve && ollama pull deepseek-r1:8b
```

## Usage

1. Add documents to `data/documents/`
2. Run the app:

```bash
python src/index.py
```
