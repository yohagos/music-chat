from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    id: int
    username: str
    password: str

class ShowUser(UserBase):
    username: str