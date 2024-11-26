from typing import List
from pydantic import BaseModel
from app.serializers.user import UserBaseSchema


class PaginatedResponse(BaseModel):
    items: List[UserBaseSchema]
    total: int
    page: int
    size: int
    pages: int
