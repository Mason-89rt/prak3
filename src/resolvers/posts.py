from src.sql_base import base_worker
from src.sql_base import models

def new_post(post: models.Post) -> int:
    new_id = base_worker.execute("INSERT INTO user(post, )"
                                     "VALUES(?,) "
                                     "RETURNING id",
                                     (post.name, ))
    return new_id
