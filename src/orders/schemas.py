from pydantic import BaseModel
from datetime import datetime


class AddOrder(BaseModel):
    order_id: int
    customer_id: int
    product_id: int
    #shipped_date: int
    ship_address: str
    ship_city: str
    ship_region: str
    ship_postal_code: str
    ship_country: str
    total_cost: int
    order_status: bool

