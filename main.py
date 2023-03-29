from enum import Enum
from typing import List

from fastapi import FastAPI, Depends
from fastapi_users import fastapi_users, FastAPIUsers
from pydantic import BaseModel

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

app = FastAPI(
    title="Social_network"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.name}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello!"






# fake_users = [
#     {'id': 1, 'user_name': 'Matthew', 'user_surname': 'Kapitonov', 'age': 26, 'gender': 'male'},
#     {'id': 2, 'user_name': 'Sergey', 'user_surname': 'Kapitonov', 'age': 55, 'gender': 'male'},
#     {'id': 3, 'user_name': 'Julia', 'user_surname': 'Kantu', 'age': 25, 'gender': 'female'},
# ]
#
#
# class GenderType(Enum):
#     male = 'male'
#     female = 'female'
#
#
# class User(BaseModel):
#     id: int
#     user_name: str
#     user_surname: str
#     age: int
#     gender: GenderType
#
#
# @app.get('/users/{user_id}', response_model=List[User])
# def get_user(user_id: int):
#     return [user for user in fake_users if user.get('id') == user_id]
#
#
# # @app.post('/users/')
# # def create_user(id: int, name: str, surname: str, age: int, sex: str):
# #
#
# @app.post('/users/{user_id}')
# def change_user_name(user_id: int, new_name: str, new_surname: str):
#     current_user = list(filter(lambda user: user.get('id') == user_id, fake_users))[0]
#     current_user['user_name'] = new_name
#     current_user['user_surname'] = new_surname
#     return {'status': 200, 'user': current_user}