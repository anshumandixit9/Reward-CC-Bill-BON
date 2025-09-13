from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def health():
    return "The app is up and working!"