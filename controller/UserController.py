from fastapi import APIRouter

router = APIRouter()

@router.get("/healthcheck")
def get_users():
    return {"message": "List of users"}
