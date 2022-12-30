from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from schemas.models import ContactRequests as ContactRequestModel, User as UserModel
from utitlities.logged_in import get_user
from utitlities.util import getTimeStamp

def accept_contact_request(request: ContactRequestModel, db: Session):
    pass

def create_new_requests(request: ContactRequestModel, db: Session):
    user = get_user()
    sender = db.query(UserModel).filter(UserModel.username == user).first()
    if request.user is request.requested:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'User {request.user} cannot request Contact to themself')
    elif sender is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {user} not found')
    # how to create sqlalchemy query with join?
# q = Session.query(
#          User, Document, DocumentPermissions,
#     ).filter(
#          User.email == Document.author,
#     ).filter(
#          Document.name == DocumentPermissions.document,
#     ).filter(
#         User.email == 'someemail',
#     ).all()

    # Check request infos!
    print(request)
    db.add(request)
    db.commit()
    db.refresh(request)
    pass

def get_request_list(db: Session):
    return db.query(ContactRequestModel).all()

def decline_contact_request(id: int, db: Session):
    pass