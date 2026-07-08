from app.commands.base_command import BaseCommand
from app.services.conversation_state_service import conversation_state_service


class GreetingCommand(BaseCommand):

    greetings = [
        "oi",
        "olá",
        "ola",
        "bom dia",
        "boa tarde",
        "opa"
    ]

    def can_handle(self, user_id: str, message: str) -> bool:
        return message.lower().strip() in self.greetings

    def handle(self, user_id: str, message: str) -> str:

        conversation_state_service.set(user_id, "menu")

        return (
            "Olá! Seja bem-vindo à Assistente Virtual do Wayne.\n\n"
            "Digite:\n"
            "1 - Ver preços\n"
            "2 - Suporte\n"
            "3 - Agendamento"
        )