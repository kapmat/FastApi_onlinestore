from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


from database import get_async_session
from products.models import Product, Category
from products.schemas import AddProduct


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("")
# @cache(expire=60)
async def get_all_products(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Product)
        result = await session.execute(query)
        return {
            200: "success",
            "data": result.scalars().all(),
            "details": None
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            500: "error",
            "data": None,
            "details": ex
        })


@router.post("")
async def add_product(new_product: AddProduct, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(Product).values(**new_product.dict())
        await session.execute(stmt)
        await session.commit()
        return {
            201: "success",
            "data": None,
            "details": "Новый товар успешно добавлен!"
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": "Не верно указаны значения!",
            "details": str(ex)
        })


@router.delete("")
async def drop_product(drop_product_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = delete(Product).where(Product.product_id == drop_product_id)
        await session.execute(stmt)
        await session.commit()
        return {
            200: "success",
            "data": None,
            "details": "Товар успешно удален!"
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            500: "error",
            "data": None,
            "details": ex
        })


@router.put("")
async def change_product(put_product_id: int, put_product: AddProduct, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = update(Product).where(Product.product_id == put_product_id).values(**put_product.dict())
        await session.execute(stmt)
        await session.commit()
        return {
            200: "success",
            "data": None,
            "details": "Товар успешно изменен!"
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": ex
        })


@router.get("/categories")
async def get_all_categories(session: AsyncSession = Depends(get_async_session)):
    query = select(Category)
    result = await session.execute(query)
    return result.scalars().all()


@router.get("/{product_id}")
async def get_product(
        product_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    query = select(Product).where(Product.product_id == product_id)
    result = await session.execute(query)
    return {
        200: "success",
        "data": result.scalars().one(),
        "details": None
    }


@router.get("/search")
async def search_product(
        tags: str,
        session: AsyncSession = Depends(get_async_session)
):
    query = select(Product).where(Product.tags == tags)
    result = await session.execute(query)
    return {
        200: "success",
        "data": result.scalars().all(),
        "details": None
}





