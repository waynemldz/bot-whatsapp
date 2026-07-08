from app.commands.base_command import BaseCommand
from app.repositories.user_repository import save_user, get_user_by_id


class NameCommand(BaseCommand):

    def can_handle(self, user_id: str, message: str) -> bool:

        message = message.lower().strip()

        return (
            message.startswith("meu nome é")
            or message == "qual é meu nome?"
            or message == "qual e meu nome?"
        )

    def handle(self, user_id: str, message: str) -> str:

        if message.lower().startswith("meu nome é"):

            nome = message[11:].strip()

            save_user(user_id, nome)

            return f"Prazer, {nome}! Vou me lembrar do seu nome."

        usuario = get_user_by_id(user_id)

        if usuario:
            return f"Seu nome é {usuario.nome}."

        return "Ainda não sei seu nome. Diga: Meu nome é ..."