from dotenv import load_env
import os

load_env()

database_url = os.getenv("DATABASE_URL")