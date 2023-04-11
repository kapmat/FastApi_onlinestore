from fastapi import FastAPI

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate

from products.router import router as router_products
from auth.router import router as router_auth
app = FastAPI(
    title="Social_network"
)


# app.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth/jwt",
#     tags=["Auth"],
# )
#
# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["Auth"],
# )

app.include_router(router_auth)
app.include_router(router_products)
# current_user = fastapi_users.current_user()




