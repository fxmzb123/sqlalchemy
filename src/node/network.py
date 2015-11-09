from node import Base
from node import Column
from node import Integer
from node import String
from node import Sequence
from node import ForeignKey
from node import relationship
from node import backref


class Network(Base):
    __tablename__ = 'network'
    id = Column(Integer, Sequence('network_id_seq'), primary_key=True)
    name = Column(String(20))
    description = Column(String(200))
    address = Column(String(25))
    type = Column(String(1))

    host_id = Column(Integer, ForeignKey('host.id'))
    host = relationship('Host',
                        backref=backref('networks', order_by=id))