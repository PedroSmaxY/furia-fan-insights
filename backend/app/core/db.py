from sqlmodel import create_engine, SQLModel, Session

from app.core.config import settings

engine = create_engine(str(settings.DB_URL), echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session