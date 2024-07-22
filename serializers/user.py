from pydantic import BaseModel, Field


class UserBaseSchema(BaseModel):
    name: str = Field(...)
    phone: str = Field(...)
    email: str
    login: str = Field(...)
    password: str = Field(...)


class CreateUserRequestModel(BaseModel):
    name: str = Field(...)
    phone: str = Field(...)
    email: str
    login: str = Field(...)
    password: str = Field(...)


class CreateUserResponseModel(BaseModel):
    id: int = Field(...)

