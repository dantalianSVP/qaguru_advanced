from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from sqlmodel import SQLModel, Field


class UserBaseSchema(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(...)
    phone: str = Field(...)
    email: str
    login: str = Field(...)
    password: str = Field(...)
    createAt: Optional[str] = None
    updatedAt: Optional[str] = None


class CreateUserRequestModel(BaseModel):
    name: str = Field(...)
    phone: str = Field(...)
    email: str
    login: str = Field(...)
    password: str = Field(...)


class CreateUserResponseModel(BaseModel):
    id: int = Field(...)


class UpdateUserResponseModel(BaseModel):
    updatedAt: Optional[str] = None


class UserUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    email: str | None = None

