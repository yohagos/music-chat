from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from authentication.oauth2 import get_current_user
from utitlities.logged_in import get_user

from controller.messages import *
from schemas.users import UserBase
from schemas.messages import *

router = APIRouter(
    prefix='/msg',
    tags=['Messages']
)

@router.get('', response_model=List[ShowMessages])
def get_messages(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return get_user_messages(db)

@router.post('')
def post_message(request: MessagesBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    print(request)

    return create_message(request, db)
    
