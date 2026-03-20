from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Literal

PlanType = Literal['basic', 'standard', 'pro']

class WaitingListCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    plan_type: PlanType

class WaitingListResponse(WaitingListCreate):
    id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
