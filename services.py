import database as _database
import models as _models

def _add_tables():
    return _database.base.metadata.create_all(bind=_database.engine)

_add_tables()