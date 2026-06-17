class HelpCommand:

    def execute(self, args, context):

        print("""
Available commands

/help
/history
/clear
/model
/exit
""")

        return True