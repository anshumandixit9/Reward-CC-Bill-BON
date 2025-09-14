from pydantic import BaseModel, field_validator
from datetime import datetime

class Bill(BaseModel):
    BillDescription: str
    CardId: int
    Month: str
    
    @field_validator('Month')
    def validate_month(cls, v):
        try:
            datetime.strptime(v, "%Y-%m")
        except ValueError:
            raise ValueError("Month must be in YYYY-MM format")
        return v
    
    class Config:
        schema_extra = {
            "example": {
                "BillDescription": "Internet Bill for September",
                "CardId": 12345,
                "Month": "2025-09"
            }
        }