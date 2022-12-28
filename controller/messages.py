from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from schemas.messages import MessagesBase
from schemas.models import Messages as MessageModel, User as UserModel
from utitlities.logged_in import get_user
from utitlities.util import getTimeStamp

def create_message(request: MessagesBase, db: Session):
    user = get_user()
    receiver = db.query(UserModel).filter(UserModel.username == request.receiver).first()
    if not receiver:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=f'Receiver not found')
    if user == request.receiver:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Users cannot send messages to themself')
    new_msg = MessageModel(receiver=request.receiver, text=request.text, send_date=getTimeStamp(), sender=user, group_id="")
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)
    return 'added new msg'

def get_user_messages(db: Session):
    user = get_user()
    msg_list = db.query(MessageModel).filter(MessageModel.sender == user).all()
    return msg_list