from account import Base
from account import Column
from account import Integer
from account import String
from account import Sequence
from account import relationship, backref, ForeignKey


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String(12), nullable=False)
    full_name = first_name + ' ' + last_name
    uuid = Column(String(12), nullable=False)
    staff_id = Column(String(12), nullable=False)
    email = Column(String(20), nullable=False)
    phone = Column(String(20), nullable=False)

    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship('Department',
                              backref=backref('users', order_by=id))

    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship('Group',
                         backref=backref('users', order_by=id))

    position_id = Column(Integer, ForeignKey('position.id'))
    position = relationship('Position',
                            backref=backref('users', order_by=id))

    user_type_id = Column(Integer, ForeignKey('user_type.id'))
    user_type = relationship('UserType',
                             backref=backref('users', order_by=id))

    def __init__(self):
        pass

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.full_name, self.password)
