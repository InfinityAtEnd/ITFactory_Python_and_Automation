"""
ORM = Object Relational Mapping
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Users(Base):
	__tablename__ = "Users"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	age = Column(Integer)


# connect to database
engine = create_engine("sqlite:///users.db")
# create all table
Base.metadata.create_all(engine)
# start session
Session = sessionmaker(bind=engine)
session = Session()
# add user
u1 = Users(name="Jhon", age=30)
u2 = Users(name="Jane", age=29)
# session.add(u1)
# session.add(u2)
session.commit()
# select
users = session.query(Users).all()
for user in users:
	print(user.id, user.name, user.age)

# update
print(60 * "*")
user = session.query(Users).filter_by(name="Jhon").first()
user.age = 31
session.commit()
users = session.query(Users).all()
for user in users:
	print(user.id, user.name, user.age)

# delete
print(60 * "*")
user = session.query(Users).filter_by(name="Jane").first()
session.delete(user)
session.commit()
users = session.query(Users).all()
for user in users:
	print(user.id, user.name, user.age)