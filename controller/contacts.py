from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from schemas.models import ContactRequests as ContactRequestModel
from utitlities.logged_in import get_user
from utitlities.util import getTimeStamp

def accept_contact_request(request: ContactRequestModel, db: Session):
    pass

def create_new_requests(request: ContactRequestModel, db: Session):
    user = get_user()
    print(request)

    # Check request infos!

    db.add(request)
    db.commit()
    db.refresh(request)
    pass

def get_request_list(db: Session):
    return db.query(ContactRequestModel).all()

def decline_contact_request(id: int, db: Session):
    pass