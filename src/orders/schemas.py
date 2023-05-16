from typing import List

from fastapi import Depends
from pydantic import BaseModel, validator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_async_session
from products.models import Product
from datetime import datetime


class ProductsCart(BaseModel):
    product_id: int
    quantity: int


class AddOrder(BaseModel):
    order_id: int
    customer_id: int
    #shipped_date: int
    ship_address: str
    ship_city: str
    ship_region: str
    ship_postal_code: int
    ship_country: str
    total_cost: int
    products: list[ProductsCart]

    # @validator('products')
    # async def quantity_valid(cls, v, session: AsyncSession = Depends(get_async_session)):
    #     for position in v:
    #         query = select(Product).units_in_stock.where(Product.product_id == position['product_id'])
    #         result = await session.execute(query)
    #         units_in_stock = result.scalars().all()
    #         position['quantity']




