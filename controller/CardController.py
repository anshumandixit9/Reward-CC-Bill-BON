from fastapi import APIRouter, HTTPException
from models.UserCard import UserCard
from services import CardService

router = APIRouter()

@router.post("/register-user-card")
async def register_user_card(user_card: UserCard):
    try:
        result = await CardService.register_user_card(user_card)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))