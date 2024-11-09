from datetime import datetime
from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    user_id: int


class PostResponse(PostBase):
    id: int
    created_at: datetime
    user_id: int
    model_config = ConfigDict(from_attributes=True)
