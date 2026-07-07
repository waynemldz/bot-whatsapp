from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config.settings import settings

engine = create_engine(settings.DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

# Importa os modelos para que o SQLAlchemy os registre
from app.models.user import Usuario

Base.metadata.create_all(bind=engine)