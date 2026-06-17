class ModelCommand:

    def execute(self, args, context):

        print(context["model"])

        return True