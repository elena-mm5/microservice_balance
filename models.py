import datetime as _dt
import sqlalchemy as _sql

import database as _database



class Account(_database.base):
    __tablename__ = "accounts"
    user_id = _sql.Column(_sql.BIGINT, primary_key=True, index=True)
    balance = _sql.Column(_sql.INT)


class Report(_database.base):
    __tablename__ = "report_accounting"
    service_id = _sql.Column(_sql.BIGINT, primary_key = True)
    year = _sql.Column(_sql.INT, primary_key = True)
    month = _sql.Column(_sql.SMALLINT, primary_key = True)
    income = _sql.Column(_sql.INT)


class Reserved(_database.base):
    __tablename__ = "reserved_accounts"
    id = _sql.Column(_sql.BIGINT, primary_key=True, index=True)
    user_id = _sql.Column(_sql.BIGINT, _sql.ForeignKey('accounts.user_id'))
    order_id = _sql.Column(_sql.BIGINT)
    service_id = _sql.Column(_sql.INT)
    cost = _sql.Column(_sql.INT)


class TransactionsHistory(_database.base):
    __tablename__ = "transaction_hictory"
    id = _sql.Column(_sql.BIGINT, primary_key=True)
    user_id = _sql.Column(_sql.BIGINT, _sql.ForeignKey('accounts.user_id'))
    operation = _sql.column(_sql.TEXT)
    comments = _sql.column(_sql.TEXT)
    time = _sql.column(_sql.DATETIME)
    amount = _sql.column(_sql.INT)


