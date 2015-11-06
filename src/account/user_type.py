from account import Base
from account import Column
from account import Integer
from account import String
from account import Sequence


class UserType(Base):
    __tablename__ = 'user_type'
    id = Column(Integer, Sequence('user_type_id_seq'), primary_key=True)
    name = Column(String(20))
    description = Column(String(200))
