from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict
from datetime import datetime
import re

class ContactBase(BaseModel):
    name: str = Field(..., max_length=255)
    phone_number: str
    email: EmailStr | None = None
    address: str | None = None

    @field_validator('phone_number')
    @classmethod
    def validate_phone(cls, v: str) -> str:
        if not re.match(r"^\+?[1-9]\d{1,14}$", v):
            raise ValueError('Invalid phone number format')
        return v

class ContactCreate(ContactBase):
    pass

class ContactUpdate(BaseModel):
    name: str | None = Field(None, max_length=255)
    phone_number: str | None = None
    email: EmailStr | None = None
    address: str | None = None
    
    @field_validator('phone_number')
    @classmethod
    def validate_phone(cls, v: str | None) -> str | None:
        if v is not None and not re.match(r"^\+?[1-9]\d{1,14}$", v):
            raise ValueError('Invalid phone number format')
        return v

class ContactResponse(ContactBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
