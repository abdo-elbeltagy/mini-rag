from fastapi import APIRouter
import os


base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)


@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME", "Mini RAG")
    app_version = os.getenv("APP_VERSION", "0.1")
    return {app_name: app_name, "version": app_version}
