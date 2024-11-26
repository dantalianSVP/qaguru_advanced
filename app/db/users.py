from typing import Iterable
import dotenv
from app.serializers.user import UserBaseSchema, UserUpdate
dotenv.load_dotenv()
from app.db.engine import engine
from sqlmodel import Session, select


def get_user(user_id: int) -> UserBaseSchema | None:
    with Session(engine) as session:
        return session.get(UserBaseSchema, user_id)


def get_users() -> Iterable[UserBaseSchema | None]:
    with Session(engine) as session:
        statement = select(UserBaseSchema)
        return session.exec(statement).all()


def create_user(user: UserBaseSchema) -> UserBaseSchema:
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(UserBaseSchema, user_id)
        session.delete(user)
        session.commit()


def update_user(user_id: int, user: UserUpdate):
    with Session(engine) as session:
        user_db = session.get(UserBaseSchema, user_id)
        user_data = user.model_dump(exclude_unset=True)
        user_db.sqlmodel_update(user_data)
        session.add(user_db)
        session.commit()
        session.refresh(user_db)
        return user_db
