from fastapi import FastAPI
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