from typing import Optional
from pydantic import EmailStr
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    customer_firstname: str
    customer_lastname: str
    address: str
    city: str
    region: str
    postal_code: int
    country: str
    phone: int

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    customer_firstname: str
    customer_lastname: str
    address: str
    city: str
    region: str
    postal_code: int
    country: str
    phone: int
