from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from schemas.models import History as HistoryModel

def new_song_added(user: str):
    print(user)