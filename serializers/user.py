from typing import Optional

from pydantic import BaseModel, Field


class UserBaseSchema(BaseModel):
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
