import datetime
from fastapi import HTTPException
from models.UserCard import UserCard
from queries import queries

async def register_user_card(db, user_card: UserCard) -> dict:
    if not user_card.UserId:
        raise HTTPException(status_code=422, detail="UserId is required")
    if not user_card.CardNumber or not user_card.CardNumber.strip():
        raise HTTPException(status_code=422, detail="CardNumber is required")
    if not (1 <= user_card.BillingDay <= 28):
        raise HTTPException(status_code=422, detail="BillingDay must be between 1 and 28")
    if not user_card.DueDays:
        raise HTTPException(status_code=422, detail="DueDays is required")

    params = {
        "userid": user_card.UserId,
        "cardnumber": user_card.CardNumber.strip(),
        "billingday": user_card.BillingDay,
        "duedays": user_card.DueDays,
        "createddate": datetime.datetime.utcnow()
    }

    try:
        sql = queries.CREATE_USER_CARD
        row = await db.fetchrow(
            sql,
            params["userid"],
            params["cardnumber"],
            params["billingday"],
            params["duedays"],
            params["createddate"]
        )
        return {"message": "User card registered successfully", "card_id": row["CardId"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing query: {str(e)}")

async def get_card_by_id(db, card_id: int):
    sql = queries.GET_CARD_BY_ID
    row = await db.fetchrow(sql, card_id)
    return dict(row) if row else None