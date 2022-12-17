from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from schemas.users import UserBase, ShowUser
from database.db import get_db
from controller.users import get_user_by_id, create_user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.get('', response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return get_user_by_id(id, db)

@router.post('', response_model=ShowUser)
def create_new_user(request: UserBase, db: Session = Depends(get_db)):
    return create_user(request, db)