from app.repositories.user_repository import get_user_by_id, save_user
from app.services.conversation_state_service import conversation_state_service


def process_message(user_id: str, message: str):

    user_message = message.lower().strip()

    if user_message.startswith("meu nome é"):

        nome = message[11:].strip()

        save_user(user_id, nome)

        return f"Prazer, {nome}! Vou me lembrar do seu nome."

    current_state = conversation_state_service.get(user_id)

    if user_message in [
        "oi",
        "olá",
        "ola",
        "bom dia",
        "boa tarde",
        "opa"
    ]:

        conversation_state_service.set(user_id, "menu")

        return (
            "Olá! Seja bem-vindo à Assistente Virtual de Whatsapp do Wayne (em fase de desenvolvimento).\n"
            "Digite:\n"
            "1 - Ver preços\n"
            "2 - Suporte\n"
            "3 - Agendamento"
        )

    if current_state == "menu":

        if user_message == "1":

            conversation_state_service.set(user_id, "precos")

            return "Nosso plano básico custa R$99 por mês."

        elif user_message == "2":

            conversation_state_service.set(user_id, "suporte")

            return "Descreva seu problema em uma única mensagem."

        elif user_message == "3":

            conversation_state_service.set(user_id, "agendamento")

            return "Qual horário você deseja?"

    if current_state == "suporte":

        conversation_state_service.clear(user_id)

        return (
            f"Entendi seu problema: {message}. "
            "Nossa equipe responderá em breve."
        )

    if user_message == "qual é meu nome?":

        usuario = get_user_by_id(user_id)

        if usuario:
            return f"Seu nome é {usuario.nome}."

        return "Você ainda não me disse seu nome."

    return "Digite 'oi' para iniciar."