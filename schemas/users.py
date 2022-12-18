from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    password: str

class ShowUser(UserBase):
    username: str

class TokenData(BaseModel):
    username: Optional[str] = None