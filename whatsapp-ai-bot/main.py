from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
user_states = {}

class Message(BaseModel):
    message:str

@app.get("/")
def home():
    return {"message":"API funcionando"}

@app.post("/message")
def receive_message(data: Message):

    user_id = "usuario_teste"

    user_message = data.message.lower().strip()

    current_state = user_states.get(user_id)

    if user_message == "oi":

        user_states[user_id] = "menu"

        return {
            "response": (
                "Olá! Seja bem-vindo à Assistente Virtual de Whatsapp do Wayne (em fase de desenvolvimento).\n"
                "Digite:\n"
                "1 - Ver preços\n"
                "2 - Suporte\n"
                "3 - Agendamento"
            )
        }

    if current_state == "menu":

        if user_message == "1":

            user_states[user_id] = "precos"

            return {
                "response": "Nosso plano básico custa R$99 por mês."
            }

        elif user_message == "2":

            user_states[user_id] = "suporte"

            return {
                "response": "Descreva seu problema em uma única mensagem."
            }

        elif user_message == "3":

            user_states[user_id] = "agendamento"

            return {
                "response": "Qual horário você deseja?"
            }

    if current_state == "suporte":
        user_states[user_id] = "usuario_teste"
        return {
            "response": (
                f"Entendi seu problema: {data.message}. "
                "Nossa equipe responderá em breve."
            )
        }

    return {
        "response": "Digite 'oi' para iniciar."
    }