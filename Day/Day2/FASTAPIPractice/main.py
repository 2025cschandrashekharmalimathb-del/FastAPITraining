from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
@app.get("/")
def home():
    return {"page":"home"}

@app.get("/about")
def about():
    return {"page":"about", "author":"Chandru"}

@app.get("/health")
def health():
    return {"status":"ok"}

#post method
@app.post("/create")
def create_something():
    return {"message":"created"}
#path method
@app.get("/students/{usn}")
def get_result(usn):
    return {"result":"Distinction", "usn":usn}

#path method with type hint
@app.get("/candidate/{rollno}")
def get_candidate(rollno:int):
    return {"result":"Distinction", "rollno":rollno,"type":str(type(rollno))}
#Pydantic model
class Item(BaseModel):
    name:str
    price:float
    in_stock:bool=True

@app.post("/items")
def create_item(item:Item):
    return {"received":item,"total_price":item.price*1.18}