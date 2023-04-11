from fastapi import APIRouter

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate


router = APIRouter(
    tags=["Auth"]
)


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
)


