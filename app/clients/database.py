from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.settings import DB_URL

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    db = SessionLocal()
    yield db
