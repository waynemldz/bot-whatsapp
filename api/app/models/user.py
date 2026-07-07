from sqlalchemy import Column, String

from database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    user_id = Column(String, primary_key=True)
    nome = Column(String)