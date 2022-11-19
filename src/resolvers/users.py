from sql_base import base_worker
from sql_base import models

def new_user(user: models.User) -> int:
    new_id = base_worker.insert_data("INSERT INTO user(login, password)"
                                     "VALUES(?,?) "
                                     "RETURNING id",
                                     (user.login, user.password))
    return new_id

