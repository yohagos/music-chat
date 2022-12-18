from pydantic import BaseModel
from typing import Optional

class MusicBase(BaseModel):
    artist: str
    title: str
    genre: str
    path: str
    uploadedBy: str

class MusicUpload(BaseModel):
    artist: str
    title: str
    genre: str

class ShowMusic(MusicBase):
    artist: str
    title: str
    genre: str
    uploadedBy: str

    class Config():
        orm_mode = True