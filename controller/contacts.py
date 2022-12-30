from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from schemas.models import ContactRequests as ContactRequestModel
from utitlities.logged_in import get_user
from utitlities.util import getTimeStamp

def accept_contact_request(db: Session):
    pass

def get_request_list(db: Session):
    return db.query(ContactRequestModel).all()

def decline_contact_request(id: int, db: Session):
    pass