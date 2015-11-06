from account import Base
from account import Column
from account import Integer
from account import String
from account import Sequence


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, Sequence('group_id_seq'), primary_key=True)
    name = Column(String(20))
    description = Column(String(200))
