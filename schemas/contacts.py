from pydantic import BaseModel

class ContactsBase(BaseModel):
    user: str
    contact: str

class ShowContacts(ContactsBase):
    class Config():
        orm_mode = True

class ContactRequestBase(BaseModel):
    requested: str

class ContactRequestFull(BaseModel):
    id: int
    user: str
    requested: str

class ShowContactRequest(ContactRequestFull):    
    class Config():
        orm_mode = True