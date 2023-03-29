from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("user_surname", String, nullable=False),
    Column("user_patronymic", String, nullable=True),
    Column("age", Integer, nullable=False),
    Column("gender", String, nullable=False),
    Column("registration_date", TIMESTAMP, default=datetime.utcnow()),
)

