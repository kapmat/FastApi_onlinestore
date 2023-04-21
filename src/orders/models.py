from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, TIMESTAMP

from auth.models import User
from products.models import Product
from database import BaseMeta


class Order(BaseMeta):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey(User.id))
    products = Column(Integer, ForeignKey(Product.product_id))
    order_date = Column(TIMESTAMP, default=datetime.utcnow())
    shipped_date = Column(Integer)
    ship_address = Column(String)
    ship_city = Column(String)
    ship_region = Column(String)
    ship_postal_code = Column(Integer)
    ship_country = Column(String)
    total_cost = Column(Float)
    order_status = Column(Boolean, default=True)
