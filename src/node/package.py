from node import Base
from node import Column
from node import Integer
from node import String
from node import Sequence
from node import Table
from node import ForeignKey
from node import relationship


class Package(Base):
    __tablename__ = 'package'
    id = Column(Integer, Sequence('package_id_seq'), primary_key=True)
    name = Column(String(20))
    version = Column(String(20))
    description = Column(String(200))
    architecture = Column(String(20))
    status = Column(String(2))
