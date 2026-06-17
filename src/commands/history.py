class HistoryCommand:

    def execute(self, args, context):

        for msg in context["history"].messages:

            print(f"{msg['role']}: {msg['content']}")

        return True