import datetime
from fastapi import HTTPException
from models.User import User
from queries import queries 

async def create_user(db, user: User) -> dict:
    if not user.UserName or not user.UserName.strip():
        raise HTTPException(status_code=422, detail="UserName is required")
    if not user.FirstName or not user.FirstName.strip():
        raise HTTPException(status_code=422, detail="FirstName is required")
    if not user.ContactNumber or not user.ContactNumber.strip():
        raise HTTPException(status_code=422, detail="ContactNumber is required")
    params = {
        "username": user.UserName.strip(),
        "firstname": user.FirstName.strip(),
        "lastname": user.LastName.strip() if user.LastName else None,
        "contactnumber": user.ContactNumber.strip(),
        "created": datetime.datetime.utcnow()
    }

    try:
        sql = queries.CREATE_USER 
        row = await db.fetchrow(
            sql,
            params["username"],
            params["firstname"],
            params["lastname"],
            params["contactnumber"],
            params["created"]
        )
        return {"message": "User created successfully", "user_id": row["UserId"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing query: {str(e)}")