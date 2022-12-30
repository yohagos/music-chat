from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from authentication.oauth2 import get_current_user
from schemas.users import UserBase
from schemas.contacts import ShowContactRequest, ContactRequestBase
from database.db import get_db
from controller.contacts import *

router = APIRouter(
    prefix='/contacts',
    tags=['Contacts']
)

@router.post('/accepts')
def accept_contact(request: ContactRequestBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    pass

@router.get('/req_list', response_model=List[ShowContactRequest])
def request_list(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return get_request_list(db)

@router.delete('/{id}')
def decline_request(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    pass

