from commands.clear import ClearCommand
from commands.help import HelpCommand
from commands.history import HistoryCommand
from commands.model import ModelCommand


COMMANDS = {
    "clear": ClearCommand(),
    "help": HelpCommand(),
    "history": HistoryCommand(),
    "model": ModelCommand(),
}


def dispatch(command_line, context):

    parts = command_line.strip().split()

    command = parts[0][1:]

    args = parts[1:]

    if command not in COMMANDS:
        print("Unknown command.")
        return True

    return COMMANDS[command].execute(args, context)