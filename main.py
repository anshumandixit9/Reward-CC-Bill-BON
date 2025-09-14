from fastapi import FastAPI
from router import user_router, card_router, bill_router

app = FastAPI()

app.include_router(user_router)
app.include_router(card_router)
app.include_router(bill_router)