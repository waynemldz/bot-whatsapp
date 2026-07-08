from app.commands.greeting_command import GreetingCommand
from app.commands.name_command import NameCommand


class CommandDispatcher:

    def __init__(self):
        self.commands = [
            NameCommand(),
            GreetingCommand()
        ]

    def dispatch(self, user_id: str, message: str):

        for command in self.commands:

            if command.can_handle(user_id, message):
                return command.handle(user_id, message)

        return None