from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return{"message" : "Hello World"}

@app.get("/posts")
def get_posts():
    return{"Data" : "This is your posts"}

@app.get("/createposts")
def create_posts(payLoad: dict = Body(...)):
    return{"new_post" : f"title {payLoad['title']} conten: {payLoad['content']}"}




