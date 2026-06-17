import json
from pathlib import Path


class HistoryManager:

    def __init__(self, history_file: Path):

        self.history_file = history_file

        self.messages = []

        self.load()

    def load(self):

        self.history_file.parent.mkdir(parents=True, exist_ok=True)

        if not self.history_file.exists():

            self.history_file.write_text(
                "[]",
                encoding="utf-8"
            )

        with open(
            self.history_file,
            "r",
            encoding="utf-8"
        ) as f:

            self.messages = json.load(f)

    def save(self):

        with open(
            self.history_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.messages,
                f,
                indent=2,
                ensure_ascii=False
            )

    def add(self, role, content):

        self.messages.append(
            {
                "role": role,
                "content": content
            }
        )

        self.save()

    def clear(self):

        self.messages.clear()

        self.save()

    def get_messages(self):

        return self.messages