import asyncpg
from contextlib import asynccontextmanager
from config import database_url

@asynccontextmanager
async def get_db_connection():
    conn = await asyncpg.connect(database_url)
    try:
        yield conn
    finally:
        await conn.close()
