from pydantic import BaseModel, validator


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
    tags: str

    @validator('unit_price', 'units_in_stock', 'units_on_order')
    def check_price(cls, value):
        if value < 0:
            raise ValueError("The value cannot be less than 0")
        return value

