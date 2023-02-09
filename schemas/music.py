from pydantic import BaseModel, FileUrl
from typing import Optional

class MusicBase(BaseModel):
    artist: str
    title: str
    featuring: str
    genre: str
    path: str
    uploaded_by: str

class MusicUpload(BaseModel):
    artist: str
    title: str
    featuring: str
    genre: str
    uploaded_by: str

class MusicInfo(BaseModel):
    artist: str
    title: str
    feature: str
    genre: str

    
class Music(MusicBase):
    class Config():
        orm_mode = True

class ShowMusic(MusicUpload):
    class Config():
        orm_mode = True

class MusicFile(BaseModel):
    file: FileUrl