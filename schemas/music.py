from pydantic import BaseModel
from typing import Optional

class MusicBase(BaseModel):
    artist: str
    title: str
    featuring: str
    genre: str
    path: str
    uploaded_by: str

class MusicList(BaseModel):
    artist: str
    title: str
    featuring: str
    genre: str
    uploaded_by: str
    
class Music(MusicBase):
    class Config():
        orm_mode = True

class MusicUpload(BaseModel):
    artist: str
    featuring: str
    title: str
    genre: str

class ShowMusic(MusicList):
    class Config():
        orm_mode = True
