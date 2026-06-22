from commands.base_command import BaseCommand


class ModelCommand(BaseCommand):

    name = "model"

    description = "Show current model"

    def execute(self, args, context):

        console = context["console"]

        ollama = context["ollama"]

        console.info(f"Current model: {ollama.model}")