import json
import requests


class OllamaClient:

    def __init__(
        self,
        url,
        model,
        timeout=300
    ):

        self.url = url

        self.model = model

        self.timeout = timeout

    def set_model(self, model):

        self.model = model

    def stream_chat(self, messages):

        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "messages": messages,
                "stream": True
            },
            stream=True,
            timeout=self.timeout
        )

        response.raise_for_status()

        for line in response.iter_lines():

            if not line:
                continue

            yield json.loads(line)