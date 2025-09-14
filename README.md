# Cash Rewards for User 
## TASK
- Build a simple backend system that simulates this flow:
    * A user should receive a mock gift card reward only if they’ve paid their last 3 bills on time.

- You can define a User, Bill, and Reward however you like. The goal is to implement:
    1. A clean API that accepts bill payments
    2. Track each bill’s due date and payment date
    3. Logic to check if last 3 bills were paid on or before the due date. Only then, generate a mock reward (e.g., “$10 Amazon Gift Card”)

- Note: You can use any language, framework, or database.

## Framework
- FastAPI

## Database
- Postgres

## Functionality Required
- Create a user in the database.
- Admin can create a bill for user, It should be a auto-billing system but as we are just focusing on the other logic we'll create this API.
- User can pay it's bill 
- User can fetch it's current bill and last paid bills based on the date range selected
- Track each bill's due date and payment date made by the use
- Reward should be given or not

## Tables Required
- User Table (UserId, Username, FirstName, LastName, ContactNumber, CreatedDate, ModifiedDate)
- Card Table (CardId, UserId, CardNumber, BillingDay, DueDateCycle)
- Bill Table (BillId, BillDescription, CardId, DueDateTime, PaidDateTime, CreatedDate)

## APIs Required
- Create User 
- Register Card For User
- Create Bill For User (This is required as we are not implementing any auto-billing based on the card registered by user)
- Get User Bills For DateRange
- Get Details For Bill
- Pay Bill
- Generate Reward based on user eligbility

## Note
- A flow which we are not including in this is that when payment is made an entry is made in payment table which can contain
    - PayemntId
    - PaymentHash from the merchant
    - Amount of the payment 
- Then that paymentId can be referenced in the bill table.
- But we are avoiding that due to time constraint.

## Example API Usage
- Endpoint
    - POST: /user/create-user
    - BODY: {
                "UserName": "anshumandx7",
                "FirstName": "Anshuman",
                "LastName": "Dixit",
                "ContactNumber": "1234567890"
            }

    - POST: /card/register-user-card
    - BODY: {
                "UserId": 2,
                "CardNumber": "1234123412341234", -- Validated based on global standard of 19 digits
                "BillingDay": 17,                 -- 1-28 considering feburary
                "DueDays": 20
            }

    - POST: /bill/create-bill
    - BODY: {
                "BillDescription": "My Description",
                "CardId": 2,
                "Month": "2024-10"
            }
    
    - POST: /bill/pay-bill
    - PARAMS: 
        1. bill_id : 2
        2. payment_id : "ywoqieywqoi32321"

    - GET: /bill/get-user-bills
    - PARAMS:
        1. user_id : 2
        2. start_month: 2024-09 -- optional
        3. end_month: 2025-10   -- optional

    - GET: /bill/bill-details
    - PARAMS:
        1. bill_id : 2

    - GET: /bill/last-3-bills-reward
    - PARAMS:
        1. user_id : 2