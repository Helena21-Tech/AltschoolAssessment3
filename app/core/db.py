from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings

# SQLite (development)
DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    echo=True if settings.ENVIRONMENT == "DEBUG" else False,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Modern Base class (SQLAlchemy 2.x)
class Base(DeclarativeBase):
    pass