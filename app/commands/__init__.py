from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command_class):
        self.commands[command_name] = command_class

    def execute_command(self, command_name: str, *args):
        try:
            command_class = self.commands[command_name]
            command = command_class(*args)
            command.execute()
        except KeyError:
            print(f"No such command: {command_name}")
