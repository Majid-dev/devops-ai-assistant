from __future__ import annotations

import json
from pathlib import Path

from core.roles import Role


class HistoryManager:
    """
    Stores and persists chat history.
    """

    def __init__(self, history_file: Path):

        self.history_file = history_file

        self.messages: list[dict] = []

        self.load()

    def load(self):

        self.history_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.history_file.exists():

            self.history_file.write_text(
                "[]",
                encoding="utf-8"
            )

        try:

            with open(
                self.history_file,
                "r",
                encoding="utf-8"
            ) as f:

                self.messages = json.load(f)

        except json.JSONDecodeError:

            self.messages = []

            self.save()

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

    def add(
        self,
        role: Role,
        content: str
    ) -> None:

        self.messages.append(

            {
                "role": role.value,
                "content": content
            }

        )

        self.save()

    def clear(self):

        self.messages.clear()

        self.save()

    def get_messages(self):

        return self.messages

    def count(self):

        return len(self.messages)