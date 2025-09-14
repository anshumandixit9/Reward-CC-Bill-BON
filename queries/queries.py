CREATE_USER = """
INSERT INTO public."Users" ("UserName", "FirstName", "LastName", "ContactNumber", "CreatedDate")
VALUES ($1, $2, $3, $4, $5)
RETURNING "UserId";
"""

CREATE_USER_CARD = """
INSERT INTO "UserCard" ("UserId", "CardNumber", "BillingDay", "DueDays", "CreatedDate")
VALUES ($1, $2, $3, $4, $5)
RETURNING "CardId";
"""

CREATE_BILL = """
INSERT INTO "Bills" ("BillDescription", "CardId", "DueDateTime", "CreatedDate", "Month")
VALUES ($1, $2, $3, $4, $5)
RETURNING "BillId";
"""

GET_BILL_BY_CARDID_MONTH = """
SELECT * FROM "Bills" WHERE "CardId" = $1 AND "Month" = $2;
"""

GET_CARD_BY_ID = """
SELECT * FROM "UserCard" WHERE "CardId" = $1;
"""

UPDATE_BILL_PAYMENT = """
UPDATE "Bills"
SET "PaidDateTime" = $1, "PaymentId" = $2
WHERE "BillId" = $3
RETURNING "BillId";
"""

GET_BILLS_BY_USER_MONTH_RANGE = """
SELECT 
    b."BillId",
    b."BillDescription",
    b."CardId",
    b."DueDateTime",
    b."PaidDateTime",
    b."CreatedDate",
    b."Month",
    b."PaymentId",
    CASE 
        WHEN b."PaidDateTime" IS NOT NULL THEN 'Paid'
        ELSE 'Unpaid'
    END AS "Status"
FROM "Bills" b
JOIN "UserCard" uc ON b."CardId" = uc."CardId"
WHERE uc."UserId" = $1
  AND b."Month" >= $2
  AND b."Month" <= $3
ORDER BY b."Month" DESC;
"""

GET_BILL_BY_ID = """
SELECT 
    "BillId",
    "BillDescription",
    "CardId",
    "DueDateTime",
    "PaidDateTime",
    "CreatedDate",
    "Month",
    "PaymentId",
    CASE 
        WHEN "PaidDateTime" IS NOT NULL THEN 'Paid'
        ELSE 'Unpaid'
    END AS "Status"
FROM "Bills"
WHERE "BillId" = $1;
"""

GET_LAST_N_BILLS_BY_USER = """
SELECT 
    b."BillId",
    b."BillDescription",
    b."DueDateTime",
    b."PaidDateTime"
FROM "Bills" b
JOIN "UserCard" uc ON b."CardId" = uc."CardId"
WHERE uc."UserId" = $1
ORDER BY b."Month" DESC
LIMIT $2;
"""