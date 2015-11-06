import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import DateTime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Sequence


class BaseEntity(object):
    __tablename__ = ''

    id = Column(Integer, Sequence(__tablename__ + '_id_seq'), primary_key=True)
    modified = Column(DateTime(), onupdate=datetime.datetime.now)
    created = Column(DateTime(), default=datetime.datetime.now)

Base = declarative_base(cls=BaseEntity)

engine = create_engine('sqlite:///:memory:', echo=True)


def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()

    return session


def create_schema():
    Base.metadata.create_all(engine)
