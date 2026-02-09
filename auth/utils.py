# created this file to hash the passwords

from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["argon2"],deprecated='auto')


# means our input is string dt and ouput is also string
def hash_password(password:str)->str:
    return pwd_context.hash(password)

# IP= str, OP= bool (yes/no) for verified
def verify_password(plain_password:str,hashed_password:str)->bool:
    return pwd_context.verify(plain_password,hashed_password)

# create the main file: main.py
