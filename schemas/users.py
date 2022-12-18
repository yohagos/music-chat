from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    password: str

class ShowUser(UserBase):
    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Login(BaseModel):
    username: str
    password: str