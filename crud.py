# status to pass the code and error message(details)
from fastapi import FastAPI,status

# for rasing an exception when the book is not found
from fastapi.exceptions import HTTPException
from pydantic import BaseModel


# list of books: our temporary database
books=[
    {
        "id":1,
        "title":"The Alchemist",
        "author":"Paulo Coelho",
        "publish_date":"1998-01-01",
    },
     {
        "id":2,
        "title":"The God of Small Things",
        "author":"Arundhati Roy",
        "publish_date":"1997-04-04",
    }, {
        "id":3,
        "title":"The White Tiger",
        "author":"Aravind Adiga",
        "publish_date":"2008-01-01",
    }, {
        "id":4,
        "title":"The palace of Illusions",
        "author":"Chitra Banerjee Divakaruni",
        "publish_date":"2008-02-12",
    },
]

app=FastAPI();


# http://127.0.0.1:8000/book using swagger ui: http://127.0.0.1:8000/docs#/default/get_book_book_get
@app.get("/book")
def get_book():
    return books


## POST METHOD:
class Book(BaseModel):
    id:int
    title:str
    author:str
    publish_date:str
    
# model_dump(): converts pydantic model into dictionary.
@app.post("/book")
def create_book(book:Book):
    new_book=book.model_dump()
    books.append(new_book)
    return new_book

# after hitting above endpoint check the get method : /book


# fetching the book with the help of id: book_id
@app.get("/book/{book_id}")
def get_book(book_id:int):
    for book in books:
        if book['id']==book_id:
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")


# update our data using PUT method: 
# we dont have to update our book id
class Book_update(BaseModel):
    title:str
    author:str
    publish_date:str

@app.put("/book/{book_id}")
# below we have the function taking the required inputs, the feature of Book_upadte us inherited in book_update variable so you can access the title like wise, all the changes u do from the frontend are stored inside the book_update variable
def update_book(book_id:int,book_update:Book_update):
    for book in books:
        if book['id']==book_id:
            book['title']=book_update.title
            book['author']=book_update.author
            book['publish_date']=book_update.publish_date
            # if you dont return anything it may cause an error
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Error while updating the book information')
            

# DELETE METHOD:
#  finding the book with the help of id and deleting, we dont need class here as it is not pydantic

@app.delete("/book/{book_id}")
# remeber that you have to pass inside the following function
def delete_book(book_id:int):
    for book in books:
        if book['id']==book_id:
            books.remove(book)
            return {"Message":"Book deleted successfully"}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Error occured while deleting the book')