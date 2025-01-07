from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello, World!"

@app.get("/greet")
def greet():
    return "welcome to git"

@app.get("/testing")
def branche():
    return "in testing branch"
