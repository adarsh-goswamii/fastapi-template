from fastapi import APIRouter, Request

from src.services.user.serializer import GetUserInBound
from src.services.user.controller import UserController

router = APIRouter()


@router.get("/")
async def get_users(request: Request, payload: GetUserInBound):
    return UserController.get_users(request, payload)

