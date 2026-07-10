from app.commands.command_dispatcher import CommandDispatcher
from app.services.ai_service import ask_ai
from app.services.conversation_state_service import conversation_state_service

dispatcher = CommandDispatcher()


def process_message(user_id: str, message: str):

    if (
        conversation_state_service.get(user_id) == "human"
        and message.lower().strip() != "/ia"
    ):
        return (
            "Você já está aguardando atendimento humano.\n"
            "Em instantes um atendente responderá sua mensagem."
        )

    response = dispatcher.dispatch(user_id, message)

    if response:
        return response

    return ask_ai(user_id, message)