from enum import Enum
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(
    title="Social_network"
)

fake_users = [
    {'id': 1, 'user_name': 'Matthew', 'user_surname': 'Kapitonov', 'age': 26, 'gender': 'male'},
    {'id': 2, 'user_name': 'Sergey', 'user_surname': 'Kapitonov', 'age': 55, 'gender': 'male'},
    {'id': 3, 'user_name': 'Julia', 'user_surname': 'Kantu', 'age': 25, 'gender': 'female'},
]


class GenderType(Enum):
    male = 'male'
    female = 'female'


class User(BaseModel):
    id: int
    user_name: str
    user_surname: str
    age: int
    gender: GenderType


@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


# @app.post('/users/')
# def create_user(id: int, name: str, surname: str, age: int, sex: str):
#

@app.post('/users/{user_id}')
def change_user_name(user_id: int, new_name: str, new_surname: str):
    current_user = list(filter(lambda user: user.get('id') == user_id, fake_users))[0]
    current_user['user_name'] = new_name
    current_user['user_surname'] = new_surname
    return {'status': 200, 'user': current_user}