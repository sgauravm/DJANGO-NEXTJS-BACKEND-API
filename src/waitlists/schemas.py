from datetime import datetime
from typing import Any, List
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


class WaitlistEntryDetailSchema(Schema):
    # Get -> Data
    # WaitlistEntryOut
    email: EmailStr
    updated: datetime
    timestamp: datetime
