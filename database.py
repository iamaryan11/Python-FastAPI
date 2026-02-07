# create engine is used to create a connection with the db
from sqlalchemy import create_engine

# whenever we make an api call a session is created:
from sqlalchemy.orm import sessionmaker

# from where all the sqlalchemy classes will be inherited:
from sqlalchemy.ext.declarative import declarative_base


# for the following variables you should keep them in the env file.
MYSQL_USER="root"
MYSQL_PASSWORD="xyz"
MYSQL_HOST="localhost"
MYSQL_PORT="3306"
MYSQL_DATABASE="my_db"

DATABASE_URI=F"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

# CONNECTION
engine=create_engine(DATABASE_URI);


# session: it is created at each api req
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

# before creating a new we need to end the previous session
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

## Base: we create a base from where all the sqlalchemy classes will be inherited
Base=declarative_base()

# create model.py