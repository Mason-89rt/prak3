from fastapi import APIRouter
from src.sql_base import Post
from src.resolvers import posts

post_router = APIRouter()
@post_router.get('/')
def get_post():
    return {'Страница со списком пероснала'}

@post_router.post('/')
def new_post(post:Post):
    new_id = posts.new_post(post)
    return f'{{code: 201, id: {new_id}}}'

@post_router.get('/{post_id}')
def get_post_id(post_id:int):
    return {post_id: 'login: gfgg'}