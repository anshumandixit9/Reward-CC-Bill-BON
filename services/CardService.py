from models.UserCard import UserCard
from common.psqlcontext import get_db_connection
from repository import CardRepository

async def register_user_card(user_card: UserCard):
    async with get_db_connection() as db:
        return await CardRepository.register_user_card(db, user_card)