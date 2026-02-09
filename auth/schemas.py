# here we will be creating our pydantic models

from pydantic import BaseModel,EmailStr


# schema for registering a user
class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str
    role:str


# schema when a user logs in: we are logging user with just two informations
class UserLogin(BaseModel):
    username:str
    password:str

# create utils.py
