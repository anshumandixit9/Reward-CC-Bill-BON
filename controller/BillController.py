from fastapi import APIRouter, HTTPException, Query
from models.Bill import Bill
from services import BillService

router = APIRouter()

@router.post("/create-bill")
async def create_bill(bill: Bill):
    try:
        result = await BillService.create_bill(bill)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/pay-bill")
async def pay_bill(bill_id: int, payment_id: str):
    try:
        result = await BillService.pay_bill(bill_id, payment_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/get-user-bills")
async def get_bills(
    user_id: int,
    start_month: str = Query(None, description="Format: YYYY-MM"),
    end_month: str = Query(None, description="Format: YYYY-MM")
):
    try:
        result = await BillService.get_bills_by_user_month_range(user_id, start_month, end_month)
        filtered = [
            {
                "BillId": bill["BillId"],
                "BillDescription": bill["BillDescription"],
                "PaidDateTime": bill["PaidDateTime"],
                "BillMonth": bill["Month"],
                "Status": bill["Status"]
            }
            for bill in result
        ]
        return filtered
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/bill-details")
async def get_bill_details(bill_id: int):
    """
    Get bill details by BillId.
    """
    try:
        bill = await BillService.get_bill_by_id(bill_id)
        if not bill:
            raise HTTPException(status_code=404, detail="Bill not found")
        return {
            "BillId": bill["BillId"],
            "BillDescription": bill["BillDescription"],
            "PaidDateTime": bill["PaidDateTime"],
            "BillMonth": bill["Month"],
            "DueDateTime": bill["DueDateTime"],
            "PaymentId": bill["PaymentId"],
            "Status": bill["Status"]
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/last-3-bills-reward")
async def last_3_bills_reward(user_id: int):
    try:
        result = await BillService.get_last_n_bills_reward(user_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
