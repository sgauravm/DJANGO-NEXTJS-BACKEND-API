from datetime import datetime
from typing import Any, List, Optional
from ninja import Schema
from pydantic import EmailStr


class WaitlistEntryCreateSchema(Schema):
    # Create -> Data
    # WaitlistEntryIn
    email: EmailStr


class ErrorWaitlistEntryCreateSchema(Schema):
    # Create -> Data
    # WaitlistEntryIn
    email: List[Any]


class WaitlistEntryListSchema(Schema):
    # List -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr
    description: Optional[str] = ""


class WaitlistEntryDetailSchema(Schema):
    # Get -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime
    description: Optional[str] = ""


class WaitlistEntryUpdateSchema(Schema):
    # PUT -> Data
    # WaitlistEntryOut
    # id: int
    description: str = ""
