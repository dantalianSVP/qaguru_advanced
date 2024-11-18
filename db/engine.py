import dotenv

dotenv.load_dotenv()
import os
from sqlalchemy.orm import Session
from sqlmodel import create_engine, SQLModel, text

engine = create_engine(os.getenv("DATABASE_ENGINE"), pool_size=int(os.getenv("DATABASE_POOL_SIZE", 10)), pool_pre_ping=True)


def create_db_and_table():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


def check_availability():
    try:
        with Session(engine) as session:
            session.execute(text("SELECT 1"))
        return True
    except Exception as e:
        print(e)
        return False
