from core.prompts import SYSTEM_PROMPT


class ChatSession:

    def __init__(
        self,
        history,
        ollama,
        console
    ):

        self.history = history

        self.ollama = ollama

        self.console = console

    def ask(self, prompt):

        messages = [

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }

        ]

        messages.extend(
            self.history.get_messages()
        )

        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        self.console.assistant_prefix()

        answer = ""

        for chunk in self.ollama.stream_chat(messages):

            if "message" not in chunk:
                continue

            content = chunk["message"].get(
                "content",
                ""
            )

            answer += content

            self.console.stream(content)

        self.console.newline()

        self.history.add(
            "user",
            prompt
        )

        self.history.add(
            "assistant",
            answer
        )

        return answer