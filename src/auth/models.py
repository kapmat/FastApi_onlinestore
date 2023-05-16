from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String, TIMESTAMP, Boolean, JSON
from sqlalchemy.orm import Mapped, mapped_column

from database import BaseMeta


class User(SQLAlchemyBaseUserTable[int], BaseMeta):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_firstname: Mapped[str] = mapped_column(String, nullable=False)
    customer_lastname: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=True)
    city: Mapped[str] = mapped_column(String, nullable=True)
    region: Mapped[str] = mapped_column(String, nullable=True)
    postal_code: Mapped[int] = mapped_column(Integer, nullable=True)
    country: Mapped[str] = mapped_column(String, nullable=True)
    phone: Mapped[int] = mapped_column(Integer, nullable=True)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    registration_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=datetime.utcnow())
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    bag: Mapped[dict] = mapped_column(JSON)
