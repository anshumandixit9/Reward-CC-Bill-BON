from models.Bill import Bill
from common.psqlcontext import get_db_connection
from repository import BillRepository
from repository import CardRepository
from datetime import datetime, timedelta

async def create_bill(bill: Bill):
    async with get_db_connection() as db:
        card = await CardRepository.get_card_by_id(db, bill.CardId)
        if not card:
            raise Exception("Card not found")
        billing_day = card["BillingDay"]
        due_days = card["DueDays"]
        year, month = map(int, bill.Month.split("-"))
        billing_date = datetime(year, month, billing_day)
        due_datetime = billing_date + timedelta(days=due_days)
        due_datetime = due_datetime.replace(hour=23, minute=59, second=59, microsecond=0)
        created_date = datetime.utcnow()
        return await BillRepository.create_bill(db, bill, due_datetime, created_date)

async def pay_bill(bill_id: int, payment_id: str):
    async with get_db_connection() as db:
        return await BillRepository.pay_bill(db, bill_id, payment_id)

async def get_bills_by_user_month_range(user_id: int, start_month: str = None, end_month: str = None):
    now = datetime.utcnow()
    if not end_month:
        end_month = now.strftime("%Y-%m")
    if not start_month:
        last_year = now - timedelta(days=365)
        start_month = last_year.strftime("%Y-%m")
    async with get_db_connection() as db:
        return await BillRepository.get_bills_by_user_month_range(db, user_id, start_month, end_month)

async def get_bill_by_id(bill_id: int):
    async with get_db_connection() as db:
        return await BillRepository.get_bill_by_id(db, bill_id)

async def get_last_n_bills_reward(user_id: int, n: int = 3):
    async with get_db_connection() as db:
        bills = await BillRepository.get_last_n_bills(db, user_id, n)
        if not bills or len(bills) < n:
            return {
                "message": "Not enough bills to evaluate reward.",
                "reward": False
            }

        all_paid_before_due = all(
            bill["PaidDateTime"] is not None and bill["PaidDateTime"] <= bill["DueDateTime"]
            for bill in bills
        )

        bill_statuses = [
            {
                "BillDescription": bill["BillDescription"],
                "PaidDateTime": bill["PaidDateTime"],
                "Status": "Paid" if bill["PaidDateTime"] else "Unpaid"
            }
            for bill in bills
        ]

        return {
            "message": "$10 Amazon Gift Card" if all_paid_before_due else "No reward",
            "bills": bill_statuses,
            "reward": all_paid_before_due
        }