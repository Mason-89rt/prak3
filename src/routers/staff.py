from fastapi import APIRouter
from src.sql_base import Staff
from src.resolvers import staffs

staff_router = APIRouter()
@staff_router.get('/')
def get_staff():
    return {'Страница со списком пероснала'}

@staff_router.post('/')
def new_staff(staff:Staff):
    new_id = staffs.new_staff(staff)
    return f'{{code: 201, id: {new_id}}}'