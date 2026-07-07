from fastapi import APIRouter
from pydantic import BaseModel

from app.services.message_service import process_message

router = APIRouter()


class Message(BaseModel):
    user_id: str
    message: str


@router.get("/")
def home():
    return {"message": "API funcionando"}


@router.post("/message")
def receive_message(data: Message):

    response = process_message(
        data.user_id,
        data.message
    )

    return {
        "response": response
    }