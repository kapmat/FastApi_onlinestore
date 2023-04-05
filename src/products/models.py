from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, Float, ForeignKey, BINARY
from sqlalchemy.orm import mapper, registry

from database import Base

# metadata = MetaData()


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String)
    description = Column(String)
    picture = Column(String)


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    category_id = Column(Integer, ForeignKey(Category.category_id))
    unit_price = Column(Float)
    units_in_stock = Column(Integer)
    units_on_order = Column(Integer)
    discontinued = Column(Boolean)
    picture = Column(String)
    description = Column(String)




#
# mapper_registry = registry()
# mapper_registry.map_imperatively(Product, products)