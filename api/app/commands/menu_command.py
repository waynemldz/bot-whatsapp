import re
import unicodedata
from difflib import get_close_matches

from app.commands.base_command import BaseCommand
from app.services.conversation_state_service import conversation_state_service


def normalize_text(text: str) -> str:
    text = text.lower().strip()

    text = "".join(
        character
        for character in unicodedata.normalize("NFD", text)
        if unicodedata.category(character) != "Mn"
    )

    # Remove pontuações como ?, !, vírgulas etc.
    text = re.sub(r"[^\w\s]", "", text)

    # Remove espaços duplicados
    return " ".join(text.split())


class MenuCommand(BaseCommand):

    def matches_trigger(
        self,
        message: str,
        triggers: set[str],
        cutoff: float = 0.80
    ) -> bool:
        if message in triggers:
            return True

        matches = get_close_matches(
            message,
            triggers,
            n=1,
            cutoff=cutoff
        )

        return bool(matches)

    price_triggers = {
        "1",
        "preco",
        "precos",
        "valor",
        "valores",
        "planos",
        "quanto custa",
        "ver precos",
        "conhecer precos",
    }

    support_triggers = {
        "2",
        "suporte",
        "ajuda",
        "preciso de ajuda",
        "quero suporte",
        "falar com suporte",
        "estou com problema",
    }

    schedule_triggers = {
        "3",
        "agendar",
        "agendamento",
        "agendar conversa",
        "agendar uma conversa",
        "quero agendar",
        "marcar reuniao",
        "marcar conversa",
        "falar com especialista",  
    }

    def can_handle(self, user_id: str, message: str) -> bool:
        normalized_message = normalize_text(message)

        return (
            self.matches_trigger(normalized_message, self.price_triggers)
            or self.matches_trigger(normalized_message, self.support_triggers)
            or self.matches_trigger(normalized_message, self.schedule_triggers)
        )

    def handle(self, user_id: str, message: str) -> str:
        normalized_message = normalize_text(message)

        if self.matches_trigger(normalized_message, self.price_triggers):
            conversation_state_service.set(user_id, "menu")

            return (
                "💎 *Nossos planos*\n\n"
                "🥉 *Plano Básico* — R$ 49,90\n"
                "Ideal para pequenas empresas.\n\n"
                "🥈 *Plano Premium* — R$ 99,90\n"
                "Mais recursos e suporte prioritário.\n\n"
                "💎 *Plano Enterprise*\n"
                "Valor sob consulta.\n\n"
                "❓ Ficou com alguma dúvida sobre os planos ou serviços?\n"
                "Estou à disposição para ajudar."
            )

        if self.matches_trigger(normalized_message, self.support_triggers):
            conversation_state_service.set(user_id, "support")

            return (
                "Certo! Descreva seu problema em uma única mensagem.\n\n"
                "Nossa equipe receberá sua solicitação."
            )

        if self.matches_trigger(normalized_message, self.schedule_triggers):
            conversation_state_service.set(user_id, "schedule")

            return (
                "Qual data e horário você deseja para o agendamento?\n\n"
                'Exemplo: "15/07 às 14h".'
            )
        return ""