from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db

router = APIRouter(
    prefix='/contacts',
    tags=['Contacts']
)

@router.post('/accepts')
def accept_contact():
    pass

@router.delete('/{id}')
def decline_request(id: int):
    pass