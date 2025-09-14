from fastapi import APIRouter, Depends
from controller import CardController, BillController, UserController

api_router = APIRouter()

# API Routers
user_router = APIRouter(prefix='/user', tags=["user"])
card_router = APIRouter(prefix='/card', tags=["card"])
bill_router = APIRouter(prefix='/bill', tags=["bill"])

# Includer Routers
user_router.include_router(UserController.router)
card_router.include_router(CardController.router)
bill_router.include_router(BillController.router)
