from fastapi import APIRouter
from sql_base.models import User
import resolvers.users

us_router = APIRouter()
#@us_router.get('/')
#def get_users():
#    return {'Страница со списком пользователей'}

@us_router.post('/')
def new_user(user: User):
    new_id = resolvers.users.new_user(user)
    return f'{{code: 201, id: {new_id}}}'

#@us_router.get('/{us_id}')
#def get_user(us_id: int):
#    return {us_id: 'login: логин, password: пароль'}
#
#@us_router.put('/{us_id}')
#def update_user(us_id: int):
#    return f'Update user {us_id}'
#
#@us_router.delete('/{us_id}')
#def delelte_user(us_id: int):
#    return f'delete user {us_id}'
