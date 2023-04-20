from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from auth.router import router as router_auth
from products.router import router as router_products
from orders.router import router as router_orders

app = FastAPI(
    title="Social_network"
)

app.include_router(router_auth)
app.include_router(router_products)
app.include_router(router_orders)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")



