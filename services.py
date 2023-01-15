from typing import TYPE_CHECKING, List, Dict

import database as _database
import models as _models
import schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _database.base.metadata.create_all(bind=_database.engine)


def get_data_base():
    data_base = _database.session_local()
    try:
        yield data_base
    finally:
        data_base.close()


async def create_user(
        user: _schemas.Account, data_base: 'Session'
) -> _schemas.Balance:
    user = _models.Account(**user.dict())
    data_base.add(user)
    data_base.commit()
    data_base.refresh(user)
    return _schemas.Balance.from_orm(user)

async def get_user(data_base: 'Session') -> Dict[_schemas.Balance]:
    users = data_base.query(_models.Account).all()
    return dict(map(_schemas.Balance.from_orm(), users))







