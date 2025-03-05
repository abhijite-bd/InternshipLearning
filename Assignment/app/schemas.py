from pydantic import BaseModel, EmailStr

class UserProfileBase(BaseModel):
    name: str
    username: str
    email: EmailStr
    phone: str

class CreateContact(UserProfileBase):
    password: str  

class Contact(UserProfileBase):
    id: int  

    class Config:
        from_attributes = True  
