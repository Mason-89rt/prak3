from fastapi import FastAPI
from sql_base import base_worker
from settings import BASE_PATH
from routers.users import us_router

base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    base_worker.create_base("C:/pythonProject/Новая папка/src/sql/base.sql")
app = FastAPI()
app.include_router(us_router, prefix='/user')

