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