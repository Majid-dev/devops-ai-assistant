from commands.base_command import BaseCommand


class ClearCommand(BaseCommand):

    name = "clear"

    description = "Clear conversation history"

    def execute(self, args, context):

        history = context["history"]

        console = context["console"]

        history.clear()

        console.success("History cleared.")