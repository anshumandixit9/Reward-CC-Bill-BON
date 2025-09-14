from models.User import User
from common.psqlcontext import get_db_connection
from repository import UserRepository

async def create_user(user: User):
    async with get_db_connection() as db:
        return await UserRepository.create_user(db, user)