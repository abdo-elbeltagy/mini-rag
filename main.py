from fastapi import FastAPI

# create the FastAPI app
app = FastAPI()

@app.get("/welcome")
def welcome():
    return {"message": "Welcome to the Mini RAG FastAPI application!"}
