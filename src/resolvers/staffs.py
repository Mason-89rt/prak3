from src.sql_base import base_worker
from src.sql_base import models

def new_staff(staff: models.Staff) -> int:
    new_id = base_worker.execute("INSERT INTO staff('id_user','surname','name','id_post')"
                                     "VALUES(?,?,?,?) "
                                     "RETURNING id",
                                     (staff.id_user, staff.surname,staff.name, staff.id_post))
    return new_id