from core.config import (
    DEFAULT_MODEL,
    HISTORY_FILE,
    OLLAMA_URL,
    REQUEST_TIMEOUT,
)

from core.history import HistoryManager
from core.ollama_client import OllamaClient
from core.chat_session import ChatSession
from core.application_context import ApplicationContext

from commands.dispatcher import CommandDispatcher

from ui.console import ConsoleUI


def build_context():

    console = ConsoleUI()

    history = HistoryManager(HISTORY_FILE)

    ollama = OllamaClient(
        url=OLLAMA_URL,
        model=DEFAULT_MODEL,
        timeout=REQUEST_TIMEOUT,
    )

    dispatcher = CommandDispatcher()

    chat = ChatSession(
        history=history,
        ollama=ollama,
        console=console,
    )

    return ApplicationContext(
        console=console,
        history=history,
        ollama=ollama,
        chat=chat,
        dispatcher=dispatcher,
    )


def main():

    context = build_context()

    context.console.info(
        "DevOps AI Assistant"
    )

    context.console.info(
        "Type 'exit' to quit."
    )

    while True:

        try:

            user_input = input("\nYou: ").strip()

            if not user_input:
                continue

            if user_input.lower() == "exit":
                break

            if user_input.startswith("/"):

                context.dispatcher.dispatch(
                    user_input,
                    context,
                )

                continue

            context.chat.ask(
                user_input
            )

        except KeyboardInterrupt:

            break

        except Exception as ex:

            context.console.error(
                str(ex)
            )


if __name__ == "__main__":

    main()