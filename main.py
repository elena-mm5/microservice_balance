from typing import TYPE_CHECKING
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services


if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()


@app.post('api/usersbalance', response_model=_schemas.Balance)
async def create_user(
    user: _schemas.Account,
    data_base: _orm.Session = _fastapi.Depends(_services.get_data_base),
):
    return await _services.create_user(user=user, data_base=data_base)


