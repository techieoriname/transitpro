from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel,EmailStr):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

