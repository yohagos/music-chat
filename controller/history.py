from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from schemas.models import History as HistoryModel

def new_song_added(user: str, id: int, db: Session):
    history = db.query(HistoryModel).filter(HistoryModel.added_by == user, HistoryModel.song_added == id).first()
    if history:
        raise HTTPException(status_code=status.HTTP_306_RESERVED, detail=f'Already exists')
    new_entry: HistoryModel = HistoryModel(song_added=id, added_by=user)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)