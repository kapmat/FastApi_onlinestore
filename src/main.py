from fastapi import FastAPI

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate

from products.router import router as router_products
from auth.router import router as router_auth

app = FastAPI(
    title="Social_network"
)

app.include_router(router_auth)
app.include_router(router_products)





