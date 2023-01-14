import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import sqlalchemy.ext.declarative as _declarative


DATABASE_URL = "postgresql+psycopg2://myuser:password@127.0.0.1:5432/usersbalance"

engine = _sql.create_engine(DATABASE_URL)

session_local = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = _declarative.declarative_base()

# base.metadata.create_all(bind=engine)
