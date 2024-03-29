from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: bool = True
    published: bool = False
    

@app.get("/")
def root():
    return{"message" : "Hello World"}

@app.get("/posts")
def get_posts():
    return{"Data" : "This is your posts"}

@app.get("/createposts")
def create_posts(new_post: Post):
    return{"data": "new post"}




