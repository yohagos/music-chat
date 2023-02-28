from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from schemas.contacts import ContactRequestBase
from schemas.models import ContactRequests as ContactRequestModel, Contacts as ContactsModel, User as UserModel
from utitlities.logged_in import get_user
from utitlities.util import getTimeStamp

def accept_contact_request(id: int, db: Session):
    user = get_user()
    con: ContactRequestModel = db.query(ContactRequestModel).filter(ContactRequestModel.id == id, ContactRequestModel.requested == user).first()
    req_con: ContactsModel = ContactsModel(user = con.user, contact = con.requested, since = getTimeStamp())
    acc_con: ContactsModel = ContactsModel(user = con.requested, contact = con.user, since = getTimeStamp())
    db.delete(con)
    db.commit()

    db.add(req_con)
    db.commit()
    db.refresh(req_con)

    db.add(acc_con)
    db.commit()
    db.refresh(acc_con)
    return 'Accepted contact request'
    
def create_new_contact_request(request: ContactRequestBase, db: Session):
    user = get_user()
    sender = db.query(UserModel).filter(UserModel.username == user).first()
    if sender is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {user} not found')
    new_con: ContactRequestModel = ContactRequestModel(user=user, requested=request.requested)
    db.add(new_con)
    db.commit()
    db.refresh(new_con)
    return 'Created new contact request'

def get_request_list(db: Session):
    user = get_user()
    return db.query(ContactRequestModel).filter(ContactRequestModel.requested == user).all()

def get_contact_list(db: Session):
    user = get_user()
    return db.query(ContactsModel).filter(ContactsModel.user == user).all()

def decline_contact_request(id: int, db: Session):
    db.query(ContactRequestModel).filter(ContactRequestModel.id == id).delete()
    db.commit()
    return f'Deleted contact request with ID {id}'

def remove_current_contact(id: int, db: Session):
    db.query(ContactsModel).filter(ContactsModel.id == id).delete()
    db.commit()
    return {'Contact removed': f'ID {id}'}

