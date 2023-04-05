from pydantic import BaseModel


class AddProduct(BaseModel):
    product_id: int
    product_name: str
    category_id: int
    unit_price: int
    units_in_stock: int
    units_on_order: int
    discontinued: bool
    picture: str
    description: str

