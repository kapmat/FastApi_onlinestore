from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis
from starlette.staticfiles import StaticFiles

from auth.router import router as router_auth
from products.router import router as router_products
from orders.router import router as router_orders
from pages.router import router as router_pages

app = FastAPI(
    title="Online_Store"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router_auth)
app.include_router(router_products)
app.include_router(router_orders)
app.include_router(router_pages)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")



