import datetime as _dt
import pydantic as _pydantic


class Balance(_pydantic.BaseModel):
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


class Accrual(Balance):

    def accrual_valide(self):
        if self.user_id <= 0:
            return 'Неверное значение user_id'

        if self.income <= 0:
            return 'Неверное значение income'

        return None


class Reservation(Balance):

    def reservation_valide(self):
        if self.user_id <= 0:
            return 'Неверное значение user_id'

        if self.order_id <= 0:
            return 'Неверное значение order_id'

        if self.service_id <= 0:
            return 'Неверное значение service_id'

        if self.cost <= 0:
            return 'Неверное значение cost'

        return None


class Account(Balance):

    def account_valide(self):
        if self.user_id <= 0:
            return 'Неверное значение user_id'


class ReportDate(Balance):
    def report_date_valide(self):
        if self.month > 12 or self.month < 1:
            return 'Неверное значение month'

        if self.year < 1900 or self.year > 2023:
            return 'Неверное значение year'

        return None


class AccountingReport(Balance):
    pass


class TransactionsHistoryParams(Balance):
    sort_date: int
    sort_sum: int
    page: int
    limit: int

    def transactions_history_params_valide(self):
        if self.user_id <=0:
            return 'Неверное значение user_id'

        if self.limit <= 0:
            return 'Неверное значение limit'

        if self.page <= 0:
            return 'Неверное значение page'

        return None


class TransactionsHistory(Balance):
    time: _dt.datetime
    amount: int
























