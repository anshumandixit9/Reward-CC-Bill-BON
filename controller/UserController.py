from typing import Any
from fastapi import APIRouter, HTTPException
from models.User import User    
from services import UserService

router = APIRouter()

@router.post("/create-user", response_model=Any)
async def create_user(user: User):
    try:
        result = await UserService.create_user(user)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=(str(e)))