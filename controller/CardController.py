from fastapi import APIRouter

# Define endpoints WITHOUT prefix
router = APIRouter()

@router.get("/healthcheck")
def get_cards():
    return {"message": "List of cards"}
