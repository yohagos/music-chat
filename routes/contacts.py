from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from authentication.oauth2 import get_current_user
from schemas.users import UserBase
from schemas.contacts import ShowContactRequest, ShowContacts, ContactRequestBase
from database.db import get_db
from controller.contacts import accept_contact_request, create_new_contact_request, \
    get_request_list, get_contact_list, decline_contact_request 

router = APIRouter(
    prefix='/contacts',
    tags=['Contacts']
)

@router.post('/accepts')
def accept_contact(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return accept_contact_request(id, db)

@router.post('/create')
def create_request(request: ContactRequestBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return create_new_contact_request(request, db)

@router.get('/req_list', response_model=List[ShowContactRequest])
def request_list(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return get_request_list(db)

@router.get('/contacts', response_model=List[ShowContacts])
def contact_list(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return get_contact_list(db)

@router.delete('/{id}')
def decline_request(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return decline_contact_request(id, db)

