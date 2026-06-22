from commands.base_command import BaseCommand


class HistoryCommand(BaseCommand):

    name = "history"

    description = "Show conversation history"

    def execute(self, args, context):

        history = context.history

        console = context.console

        messages = history.get_messages()

        if not messages:

            console.info("History is empty.")

            return

        console.info("")

        for message in messages:

            role = message["role"]

            content = message["content"]

            console.info(f"{role}: {content}")

        console.info("")