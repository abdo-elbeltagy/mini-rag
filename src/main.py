from fastapi import FastAPI
from dotenv import load_dotenv
from routes import base
# create the FastAPI app
app = FastAPI()
app.include_router(base.base_router) 