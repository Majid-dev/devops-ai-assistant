class ClearCommand:

    def execute(self, args, context):

        context["history"].messages.clear()

        context["history"].save()

        print("History cleared.")

        return True