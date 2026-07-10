from app.commands.base_command import BaseCommand
from app.services.conversation_state_service import conversation_state_service
from app.services.ticket_service import ticket_service


class HumanCommand(BaseCommand):

    triggers = [
        "atendente",
        "humano",
        "falar com atendente",
        "quero falar com atendente",
        "falar com humano"
    ]

    def can_handle(self, user_id: str, message: str) -> bool:
        return message.lower().strip() in self.triggers

    def handle(self, user_id: str, message: str) -> str:
        ticket = ticket_service.create(user_id)

        conversation_state_service.set(user_id, "human")

        return (
            "Perfeito! 😊\n\n"
            f"Seu atendimento foi registrado sob o protocolo #{ticket.id}.\n"
            "Vou encaminhar sua conversa para um atendente."
        )