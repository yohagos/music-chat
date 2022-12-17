from pydantic import BaseModel
from typing import Optional

class MusicBase(BaseModel):
    id: int
    artist: str
    title: str
    path: str
    uploadedBy: str