from app.commands.command_dispatcher import CommandDispatcher
from app.services.ai_service import ask_ai

dispatcher = CommandDispatcher()


def process_message(user_id: str, message: str):

    response = dispatcher.dispatch(user_id, message)

    if response:
        return response

    return ask_ai(message)