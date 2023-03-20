from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

# used to store all products and how many there are left to sale
class Products(Base):
	__tablename__ = "Products"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	price = Column(Integer)
	quantity = Column(Integer)

# used to store all users/clients, their current money and the shopping cart
class Users(Base):
	__tablename__ = "Users"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	money = Column(Integer)
	cart_number = Column(Integer)

# used to store the shopping carts and how much each one costs based on the items added into it
class Carts(Base):
	__tablename__ = "Carts"
	cart_number = Column(Integer)
	owner = Column(String)
	cost = Column(Integer)
	cart_id = Column(Integer, primary_key=True)

# used to store items that are added in the shopping carts by users/clients
class CartItems(Base):
	__tablename__ = "CartItems"
	cart_id = Column(Integer, primary_key=True)
	cart_number = Column(Integer)
	product = Column(String)
	quantity = Column(Integer)

# connect to database
engine = create_engine("sqlite:///online_shop.db")
# create all table
Base.metadata.create_all(engine)
# start session
Session = sessionmaker(bind=engine)
session = Session()


