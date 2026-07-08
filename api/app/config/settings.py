from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parents[3]

load_dotenv(BASE_DIR / ".env")


class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    BOT_NAME = os.getenv("BOT_NAME")
    API_HOST = os.getenv("API_HOST")
    API_PORT = int(os.getenv("API_PORT", "8000"))
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    


settings = Settings()