from fastapi import FastAPI
from src.sql_base import base_worker
from src.settings import BASE_PATH
from src.routers.staff import staff_router
from src.routers.post import post_router
from src.routers.users import user_pouter
base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    base_worker.create_base("D:/pythonProject/f1/sql/base.sql")

app = FastAPI()

@app.get("/")
def main_page():
    return {'page': 'Connection in correct'}

app.include_router(staff_router, prefix='/staff')
app.include_router(post_router, prefix='/post')
app.include_router(user_pouter, prefix='/users')



