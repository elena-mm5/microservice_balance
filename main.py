from typing import TYPE_CHECKING
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services


if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()


@app.get('/')
async def DataBase():
    return 'Welcome to Data Base'




