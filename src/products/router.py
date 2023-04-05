from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User
from database import get_async_session
from products.models import Product, Category
from products.schemas import AddProduct

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/")
async def add_product(new_product: AddProduct, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Product).values(**new_product.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/")
async def get_all_products(session: AsyncSession = Depends(get_async_session)):
    query = select(Product)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/categories")
async def get_all_categories(session: AsyncSession = Depends(get_async_session)):
    query = select(Category)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/{product_id}")
async def get_product(product_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Product).where(Product.product_id == product_id)
    result = await session.execute(query)
    return result.scalars().all()




