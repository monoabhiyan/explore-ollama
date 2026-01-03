from pathlib import Path

# Project paths - ROOT is the parent of src/
ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "data" / "documents"
CHROMA_DIR = ROOT / "chroma_db"
