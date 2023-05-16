from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, TIMESTAMP, JSON

from auth.models import User
from products.models import Product
from database import BaseMeta


# class ProductsCart(BaseMeta):
#     __tablename__ = "products_cart"
#     products_cart_id = Column(Integer, primary_key=True)
#     product_id = Column(Integer, ForeignKey(Product.product_id))
#     quantity = Column(Integer)


class Order(BaseMeta):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey(User.id))
    order_date = Column(TIMESTAMP, default=datetime.utcnow())
    shipped_date = Column(Integer)
    ship_address = Column(String)
    ship_city = Column(String)
    ship_region = Column(String)
    ship_postal_code = Column(Integer)
    ship_country = Column(String)
    total_cost = Column(Integer)
    order_status = Column(Boolean, default=True)
    products = Column(JSON)
    # product_cart = Column(Integer, ForeignKey(ProductsCart.products_cart_id))