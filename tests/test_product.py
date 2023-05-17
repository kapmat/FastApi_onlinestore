import pytest
from sqlalchemy import insert, select

from products.models import Category, Product
from conftest import client, async_session_maker


async def test_add_category():
    async with async_session_maker() as session:
        stmt = insert(Category).values(category_id=1,
                                       category_name="test_name",
                                       description="test_description",
                                       picture="test_picture")
        await session.execute(stmt)
        await session.commit()

        query = select(Category)
        result = await session.execute(query)
        print(result.scalars().one())


def test_add_product():
    response = client.post("/products", json={
        "product_id": 1,
        "product_name": "test_name",
        "category_id": 1,
        "unit_price": 0,
        "units_in_stock": 0,
        "units_on_order": 0,
        "discontinued": True,
        "picture": "string",
        "description": "string",
        "tags": "string"
    })

    assert response.status_code == 200