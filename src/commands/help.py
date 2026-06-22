from commands.base_command import BaseCommand


class HelpCommand(BaseCommand):

    name = "help"

    description = "Show available commands"

    def execute(self, args, context):

        console = context["console"]

        dispatcher = context["dispatcher"]

        console.info("")

        console.info("Available Commands")

        console.info("----------------------------")

        for command in dispatcher.commands.values():

            console.info(
                f"/{command.name:<12} {command.description}"
            )

        console.info("")