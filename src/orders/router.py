from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from orders.models import Order
from orders.schemas import AddOrder


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get("/")
async def get_all_orders(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Order)
        result = await session.execute(query)
        return {
            200: "success",
            "data": result.scalars().all(),
            "details": None
        }
    except HTTPException as ex:
        return {
            500: "error",
            "data": None,
            "details": ex
        }


@router.post("/")
async def add_order(new_order: AddOrder, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(Order).values(**new_order.dict())
        await session.execute(stmt)
        await session.commit()
        return {
            201: "success",
            "data": None,
            "details": f"Заказ создан!"
        }
    except HTTPException as ex:
        return {
            500: "error",
            "data": None,
            "details": ex
        }
