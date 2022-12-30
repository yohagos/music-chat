from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Raw Messages

class MessagesBase(BaseModel):
    sender: str
    receiver: str
    text: str

class ShowMessages(MessagesBase):
    class Config():
        orm_mode = True

# Group

class MessageGroupBase(BaseModel):
    con_name: str

class ShowMessageGroup(MessageGroupBase):
    class Config():
        orm_mode = True

# Group Member

class GroupMemberBase(BaseModel):
    joined_time: str
    left_time: str

class ShowGroupMember(GroupMemberBase):
    class Config():
        orm_mode = True