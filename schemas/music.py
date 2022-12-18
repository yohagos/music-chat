from pydantic import BaseModel
from typing import Optional

class MusicBase(BaseModel):
    id: int
    artist: str
    title: str
    genre: str
    path: str
    uploadedBy: str

class ShowMusic(MusicBase):
    artist: str
    title: str
    genre: str
    uploadedBy: str