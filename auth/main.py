from fastapi import FastAPI,Depends,HTTPException,status

from sqlalchemy.orm import Session

# import all supporting files: schemas for pydantic classes
import models,schemas,utils
from auth_database import get_db
from jose import jwt 
from datetime import datetime,timedelta

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from jose import JWTError

# keep all these variables in the .env file
SECRET_KEY=""
ALGORITHM=''
ACCESS_TOKEN_EXPIRE_MINUTES=30


# helper function that takes the user data and create a toke, jis user data ki mdad se hum token create kr rhe hai wo dictornary k form me hai so: dict
def create_access_token(data:dict):
    # we always copy data so that we dont acidentally delete our org data
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # 'exp' is the writing converntion which jwt actually uses for expire time
    to_encode.update({'exp':expire})

    # below to_encode actually contains the user data with which we are creating the token
    encode_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt




app=FastAPI()

# Lets create our POST route to signup users:
# since, it is a POST METHOD so we will be using pydantic class which we have already created inside schemas.py so we have imported it from there, user:schemas.UserCreate <-- it is just like inheriting from a variable you have already seen that
@app.post("/signup")
def register_user(user:schemas.UserCreate, db:Session=Depends(get_db)):

    # check if the user exists or not
    existing_user=db.query(models.User).filter(models.User.username==user.username).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="User already exists")

    # else hash the password we already have that function in utils
    hashed_pass=utils.hash_password(user.password)

    # create a new user instance (naya user create kiya bss)
    new_user=models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pass,
        role=user.role
    )

    # save the user to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # return the value (except the password)
    return {'id':new_user.id,"username":new_user.username,'email':new_user.email,'role':new_user.role}


# creating the login endpoint: for this we need to import something that fastapi can automatically parse the credentials data from login form: from fastapi.security import OAuth2PasswordRequestForm

@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.username==form_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid username")
    

    # here we know we have already created the verify_password inside the utils file, so we are passing the password what user types in the form and the one which is stored in the database
    if not utils.verify_password(form_data.password,user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid creds')
    
    # but if the password is correct create the token, here again 'sub' is a naming convention for username in JWT
    token_data={'sub':user.username,'role':user.role}
    token=create_access_token(token_data)
    return {"access_token":token,"token_type":"bearer"}

# since this file contains api so to run it: uvicorn main:app --reload, before this we have to run auth_table file to create a user, then only we can store the info about user
# python auth_table.py

# test the singup and login routes using the swagger ui/postman
# when u hit the login endpoint you can observe the a form like swagger ui


# now our token is generated we will pass that token in the function:






# create key.py