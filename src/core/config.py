from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/chat"

MODEL = "qwen3"

DATA_DIR = Path("data")

HISTORY_FILE = DATA_DIR / "history.json"