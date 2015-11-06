from node import Base
from node import Column
from node import Integer
from node import String
from node import Sequence


class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer, Sequence('host_id_seq'), primary_key=True)
    name = Column(String(20))
    ip = Column(String(20))
    description = Column(String(200))
    uuid = Column(String(20))
    security_group = Column(String(20))
    default_ssh_account = Column(String(20))
    os_version = Column(String(20))
