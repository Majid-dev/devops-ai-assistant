from commands.help import HelpCommand
from commands.clear import ClearCommand
from commands.history import HistoryCommand
from commands.model import ModelCommand


class CommandDispatcher:

    def __init__(self):

        self.commands = {}

        self.register(HelpCommand())
        self.register(ClearCommand())
        self.register(HistoryCommand())
        self.register(ModelCommand())

    def register(self, command):

        self.commands[command.name] = command

    def dispatch(self, text, context):

        parts = text.strip().split()

        if not parts:
            return False

        command_name = parts[0][1:]

        args = parts[1:]

        command = self.commands.get(command_name)

        if command is None:

            context.console.error(
                f"Unknown command: {command_name}"
            )

            return True

        command.execute(args, context)

        return True