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