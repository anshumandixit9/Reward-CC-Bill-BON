from fastapi import HTTPException
from models.Bill import Bill
from queries import queries
from datetime import datetime

async def create_bill(db, bill: Bill, due_datetime, created_date):
    row = await db.fetchrow(
        queries.GET_BILL_BY_CARDID_MONTH,
        bill.CardId,
        bill.Month
    )
    if row:
        raise HTTPException(status_code=409, detail="Bill already exists for this card and month")
    result = await db.fetchrow(
        queries.CREATE_BILL,
        bill.BillDescription,
        bill.CardId,
        due_datetime,
        created_date,
        bill.Month
    )
    return {"message": "Bill created successfully", "bill_id": result["BillId"]}

async def pay_bill(db, bill_id: int, payment_id: str):
    bill = await db.fetchrow('SELECT "PaidDateTime" FROM "Bills" WHERE "BillId" = $1;', bill_id)
    if not bill:
        raise HTTPException(status_code=404, detail="Bill not found")
    if bill["PaidDateTime"] is not None:
        raise HTTPException(status_code=409, detail="Bill is already paid")
    paid_datetime = datetime.utcnow()
    row = await db.fetchrow(
        queries.UPDATE_BILL_PAYMENT,
        paid_datetime,
        payment_id,
        bill_id
    )
    return {"message": "Bill paid successfully", "bill_id": row["BillId"]}

async def get_bills_by_user_month_range(db, user_id: int, start_month: str, end_month: str):
    print(user_id, start_month, end_month)
    rows = await db.fetch(
        queries.GET_BILLS_BY_USER_MONTH_RANGE,
        user_id,
        start_month,
        end_month
    )
    print (rows)
    return [dict(row) for row in rows]

async def get_bill_by_id(db, bill_id: int):
    row = await db.fetchrow(queries.GET_BILL_BY_ID, bill_id)
    return dict(row) if row else None

async def get_last_n_bills(db, user_id: int, n: int = 3):
    rows = await db.fetch(
        queries.GET_LAST_N_BILLS_BY_USER,
        user_id,
        n
    )
    return [dict(row) for row in rows]