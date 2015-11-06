from database import Base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import aliased
from sqlalchemy import Table, Text


class HostPackage(Base):
    __tablename__ = 'host_package'
    id = Column(Integer, Sequence('host_package_id_seq'), primary_key=True)

    host_id = Column(Integer, ForeignKey('host.id'))
    host = relationship('Host', backref=backref('host_packages', order_by=id))

    package_id = Column(Integer, ForeignKey('package.id'))
    package = relationship('Package',
                           backref=backref('host_packages', order_by=id))

    description = Column(String(200))
