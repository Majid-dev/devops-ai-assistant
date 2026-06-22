from abc import ABC, abstractmethod


class BaseCommand(ABC):

    name = ""
    description = ""

    @abstractmethod
    def execute(self, args, context):
        pass