from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config.settings import settings

engine = create_engine(settings.DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

# Importa os modelos após criar o Base
from app.models.user import Usuario
from app.models.conversation_state import ConversationState

Base.metadata.create_all(bind=engine)