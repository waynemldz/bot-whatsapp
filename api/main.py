from fastapi import FastAPI
from app.routes.message_routes import router

app = FastAPI()

app.include_router(router)