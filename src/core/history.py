import json
from pathlib import Path


class History:

    def __init__(self, history_file: Path):
        self.history_file = history_file
        self.messages = []

        self.load()

    def load(self):

        if not self.history_file.exists():

            self.history_file.parent.mkdir(parents=True, exist_ok=True)

            self.history_file.write_text("[]")

        with open(self.history_file, "r", encoding="utf8") as f:

            self.messages = json.load(f)

    def save(self):

        with open(self.history_file, "w", encoding="utf8") as f:

            json.dump(
                self.messages,
                f,
                indent=2,
                ensure_ascii=False
            )

    def add(self, role, content):

        self.messages.append({
            "role": role,
            "content": content
        })

        self.save()

    def get(self):

        return self.messages