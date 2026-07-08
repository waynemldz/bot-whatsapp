from app.commands.base_command import BaseCommand
from app.services.conversation_state_service import conversation_state_service


class SupportCommand(BaseCommand):

    def can_handle(self, user_id: str, message: str) -> bool:
        return conversation_state_service.get(user_id) == "support"

    def handle(self, user_id: str, message: str) -> str:

        conversation_state_service.clear(user_id)

        return (
            "Sua solicitação foi registrada com sucesso!\n\n"
            "Nossa equipe entrará em contato em breve."
        )