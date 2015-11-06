from account.position import Position
from account.group import Group
from database import create_schema
from database import create_session
from account.department import Department
from account.user_type import UserType
from account.user import User

from node.host import Host
from node.package import Package
from node import HostPackage

''' class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', backref=backref('addresses', order_by=id))


post_keywords = Table('post_keywords', Base.metadata,
                      Column('post_id', Integer, ForeignKey('posts.id')),
                      Column('keyword_id', Integer, ForeignKey('keywords.id')))


class BlogPost(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    headline = Column(String(255), nullable=False)
    body = Column(Text)

    keywords = relationship('Keyword',
                            secondary=post_keywords, backref='posts')

    def __init__(self, headline, body, author):
        self.author = author
        self.headline = headline
        self.body = body

    def __repr__(self):
        return "BlogPost(%r, %r, %r)" % (self.headline, self.body, self.author)


class Keyword(Base):
    __tablename__ = 'keywords'

    id = Column(Integer, primary_key=True)
    keyword = Column(String(50), nullable=False, unique=True)

    def __init__(self, keyword):
        self.keyword = keyword

BlogPost.author = relationship('User',
                               backref=backref('posts', lazy='dynamic'))
'''
create_schema()
session = create_session()

manager = Position(name='manager', description='manager')
senior_manager = Position(name='senior manager',
                          description='senior manager')

session.add(manager)
session.add(senior_manager)

group1 = Group(name='group1', description='group1')
group2 = Group(name='group2', description='group2')

department1 = Department(name='accounting',
                         description='department of accounting')
department2 = Department(name='marine', description='school of marine science')


usertype1 = UserType(name='registered', description='registered users')
usertype2 = UserType(name='admin', description='registered users')

session.add(manager)
session.add(senior_manager)

session.add(group1)
session.add(group2)

session.add(department1)
session.add(department2)

session.add(usertype1)
session.add(usertype1)


user = User()
user.username = 'fxmzb123'
user.first_name = 'ming'
user.last_name = 'fu'
user.password = '123456'

user.uuid = '1234567890'
user.staff_id = '123456'
user.email = 'xiao.fu@utas.edu.au'
user.phone = '62266217'

user.department = department2
user.position = manager
user.group = group1
user.user_type = usertype1


host = Host()

host.name = 'host1'
host.default_ssh_account = 'ubuntu'
host.description = 'ubuntu vm'
host.os_version = 'ubuntu 11.10'
host.uuid = '12345678'
host.ip = '12.12.12.12'
host.security_group = 'security group1'

package = Package()

package.name = 'zip'
package.architecture = 'ammd64'
package.description = 'zip function'
package.version = '1.0'
package.status = 'installed'


session.add(package)
session.add(host)

host_package = HostPackage()
host_package.host = host
host_package.package = package
host_package.description = 'many to many'

session.add(user)

session.commit()

for h in session.query(Host).order_by(Host.id):
    print h.name
    print h.created
    print h.modified
    for h_p in h.host_packages:
        print h_p.package.name
'''
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
ed_user1 = User(name='ed1', fullname='Ed Jones1', password='edspassword')

ed_user.addresses = [Address(email_address='jack@google.com'), Address(email_address='j25@yahoo.com')]
ed_user1.addresses = [Address(email_address='abc@google.com')]

session.add(ed_user)
session.add(ed_user1)
session.commit()

users = session.query(User).join(Address).\
    filter(Address.email_address == 'abc@google.com').\
    all()

print users

stmt = session.query(Address).\
    filter(Address.email_address != 'abc@google.com').\
    subquery()

adalias = aliased(Address, stmt)

for user, address in session.query(User, adalias).\
        join(adalias, User.addresses):
    print user
    print address

wendy = session.query(User).filter_by(name='wendy') '''

'''session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()

our_user.password = 'f8s7ccs'

session.commit()

our_user.name = 'Edwardo'

fake_user = User(name='fakeuser', fullname='Invalid', password='12345')
session.add(fake_user)

session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()

session.rollback()

print ed_user.name

print fake_user in session'''
