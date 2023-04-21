from typing import List

from pydantic import BaseModel
from datetime import datetime


# class ProductsCart(BaseModel):
#     product_id: int


class AddOrder(BaseModel):
    order_id: int
    customer_id: int
    products: int
    #shipped_date: int
    ship_address: str
    ship_city: str
    ship_region: str
    ship_postal_code: int
    ship_country: str
    total_cost: float


