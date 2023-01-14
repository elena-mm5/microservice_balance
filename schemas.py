import datetime as _dt
import pydantic as _pydantic


class _Balance(_pydantic.BaseModel):
    user_id: int
    balance: int
    service_id: int
    year: int
    month: int
    income: int
    order_id: int
    cost: int
    operation: str
    comments: str
    amount: int


class TransactionsHistoryParams(_Balance):
    sort_date: int
    sort_sum: int
    page: int
    limit: int


class TransactionsHistory(_Balance):
    time: _dt.datetime
    amount: int











