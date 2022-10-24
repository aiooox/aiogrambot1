from sqlalchemy import Column, BigInteger, String, sql

from utils.dbapi.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    fist_name = Column(String(200))
    last_name = Column(String(200))
    username = Column(String(200))
    update_name = Column(String(50), primary_key=True)
    status = Column(String(30))

    queue: sql.select
