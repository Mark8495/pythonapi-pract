from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{"message" : "Hello World"}

@app.get("/posts")
def get_posts():
    return{"Data" : "This is your posts"}