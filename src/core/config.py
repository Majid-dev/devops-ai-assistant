from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/chat"

DEFAULT_MODEL = "qwen3"

REQUEST_TIMEOUT = 300

DATA_DIR = Path("data")

HISTORY_FILE = DATA_DIR / "history.json"