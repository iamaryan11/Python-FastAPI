from fastapi import FastAPI,Depends
from database import get_db,engine
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel


app=FastAPI()


# Our pydantic class for post method
class Bookstore(BaseModel):
    id:int
    title:str
    author:str
    publish_date:str

@app.post('/books')

# we have already seen the inerherit variable, Session if from get_db
def create_book(book:Bookstore, db:Session=Depends(get_db)):
    new_book=model.Book(id=book.id, title=book.title,author=book.author,publish_date=book.publish_date)

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# okay so since this file includes an api so we will run this file using uvicorn as we have seen earlier: uvicorn project:app --reload


# get route for books:
@app.get('/books')
def get_book(db:Session=Depends(get_db)):
    books=db.query(model.Book).all()
    return books