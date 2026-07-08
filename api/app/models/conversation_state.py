from sqlalchemy import Column, String, DateTime
from datetime import datetime

from database import Base


class ConversationState(Base):
    __tablename__ = "conversation_states"

    user_id = Column(String, primary_key=True)
    state = Column(String, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)