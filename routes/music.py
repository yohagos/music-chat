from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from schemas.music import MusicBase, ShowMusic
from database.db import get_db

router = APIRouter(
    prefix='/music',
    tags=['Music']
)

@router.post('', response_model=ShowMusic)
async def add_new_song(request: MusicBase, db: Session = Depends(get_db)):
    pass

@router.get('', response_model=ShowMusic)
def get_song_by_id(id: int, db: Session = Depends(get_db)):
    pass

