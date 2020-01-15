from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
    "root",
    "knakajima",
    "localhost",
    "mydb3",
)

ENGINE = create_engine(
    SQLALCHEMY_DATABASE_URI,
    encoding = "utf-8",
    echo=True # Trueだと実行のたびにSQLが出力される
)

# Sessionの作成
session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE)
)

Base = declarative_base()
Base.query = session.query_property()