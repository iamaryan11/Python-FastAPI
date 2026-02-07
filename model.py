from sqlalchemy import Column,Integer,VARCHAR

# import Base from the database.py
from database import Base


# Our class: table with the help of sqlalchemy
# table name should be written like: __tablename__ only
class Book(Base):
    __tablename__="books"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(VARCHAR(255))
    author=Column(VARCHAR(255))
    publish_date=Column(VARCHAR(255))

# to proceed create: create_table.py, now go to workbench and refresh the db, you should see the table gets created

# to insert some data to ur db lets create another file called as : project.py we will create the api in this file...

