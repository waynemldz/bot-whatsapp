from app.commands.base_command import BaseCommand
from app.services.conversation_state_service import conversation_state_service


class EndHumanCommand(BaseCommand):

    def can_handle(self, user_id: str, message: str) -> bool:
        return message.lower().strip() == "/ia"

    def handle(self, user_id: str, message: str) -> str:

        conversation_state_service.clear(user_id)

        return (
            "Atendimento humano encerrado.\n\n"
            "A Assistente Virtual voltou a atender esta conversa. 🤖"
        )