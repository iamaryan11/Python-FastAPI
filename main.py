from fastapi import FastAPI

# to make some fields optional
from typing import Optional

# for post methods and pydantic class:
from pydantic import BaseModel

# this app is the instance of our fastapi object
app=FastAPI() 


# creating the route: / is the endpoin, this is our homepage

@app.get("/")
def read_root():
    return{"Message":"Hello World, trigger for reload"}

# to run this: uvicorn main:app
# to automatically save and reload changes: uvicorn main:app  --reload

@app.get("/greet")
def greet():
    return {"Message":"Hello from greet"}


## path paramter: pass the value from the url (you know): http://127.0.0.1:8000/greet/aryan
@app.get("/greet/{name}")
def greet_name(name:str):
    return {"Mesage":f"Hello {name}"}


# query parameter: ahead of the url: url/?age=20, we dont need to pass anything in the curly braces, below we have name as path param and age as query param, if we dont pass it, it will say field required: http://127.0.0.1:8000/say/rahul?age=25
# below name is path param, age is query param
@app.get("/say/{name}")
def say(name:str,age:int):
    return {'Message':f"Hello from say {name} and your age is {age}"}

# to have some fields as optional: from typing import Optional, None is the optional value.
@app.get("/greet/optional/{name}")
def say_optional(name:str, age:Optional[int]=None):
    return {'Message':f"Hello say my name {name} and here age is optional {age}"}

# multiple query params: http://127.0.0.1:8000/mutliple/query?name=luv&age=22, we start our query param we ? and seperate multiple with & operator as above
@app.get("/mutliple/query")
def multiple_query(name:str,age:Optional[int]=None):
    return {'Message':f"Hello from multiple query params name is {name} and age is {age}"}


# POST METHODS : 
# when we want to save something to our database, in this scenario request body comes in consideration. request is a JSON format data and fastapi uses pydantic for validating and parsing this data. so we dont have to write any validation code over here.
# we need to write pydantic class, we need a basemodel for that we will import as: from pydantic import BaseModel, then inherit this base model in the student class below.
# we use pydantic for post and put methods
class Student(BaseModel):
    name:str
    age:int
    roll:int

@app.post("/create_student")
# every feature of Student class is inherited in student variable as : student:Student
def create_student(student:Student):
    return {
        "name":student.name,
        "age":student.age,
        "roll":student.roll
    }

# CRUDS operations