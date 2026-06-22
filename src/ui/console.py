from rich.console import Console

console = Console()
from rich.console import Console

from ui.formatter import Formatter


class ConsoleUI:

    def __init__(self):

        self.console = Console()

    def line(self):

        self.console.print()

    def info(self, text):

        self.console.print(
            Formatter.title(text)
        )

    def success(self, text):

        self.console.print(
            Formatter.success(text)
        )

    def error(self, text):

        self.console.print(
            Formatter.error(text)
        )

    def assistant_prefix(self):

        self.console.print(
            "\nAssistant:",
            end=" "
        )

    def user_prefix(self):

        self.console.print(
            "\nYou:",
            end=" "
        )

    def stream(self, text):

        self.console.print(
            text,
            end=""
        )

    def newline(self):

        self.console.print()