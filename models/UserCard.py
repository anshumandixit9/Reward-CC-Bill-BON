from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserCard(BaseModel):
    UserId: int
    CardNumber: str = Field(..., max_length=19)
    BillingDay: int = Field(..., ge=1, le=28)
    DueDays: int