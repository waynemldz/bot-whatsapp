from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal, Usuario
from app.repositories.user_repository import get_user_by_id, save_user
from app.services.message_service import process_message

app = FastAPI()
db = SessionLocal()
user_states = {}
user_names = {}

class Message(BaseModel):
    user_id: str
    message:str

@app.get("/")
def home():
    return {"message":"API funcionando"}

@app.post("/message")
def receive_message(data: Message):

    response = process_message(
        data.user_id,
        data.message
    )

    return {
        "response": response
    }