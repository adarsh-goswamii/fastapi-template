from fastapi import APIRouter
from src.routes.v1 import user

api_router = APIRouter()

api_router.include_router(user.router, prefix='/v1/user', tags=["User"])