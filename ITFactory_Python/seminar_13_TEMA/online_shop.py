from prettytable import PrettyTable
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

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


def database_read_all():
	products = session.query(Products).all()
	prod = PrettyTable(["Product ID", "Product Name", "Product Price", "Quantity Left"])
	prod.title = "Table for PRODUCTS"
	for p in products:
		prod.add_row([p.id, p.name, p.price, p.quantity])
	print(90 * "*")
	print(prod)
	users = session.query(Users).all()
	use = PrettyTable(["User ID", "User Name", "User Money", "User Cart Number"])
	use.title = "Table for USERS"
	for u in users:
		use.add_row([u.id, u.name, u.money, u.cart_number])
	print(90 * "*")
	print(use)
	carts = session.query(Carts).all()
	cart = PrettyTable(["Cart Number", "Owner", "Total Cost", "Cart ID"])
	cart.title = "Table for CARTS"
	for c in carts:
		cart.add_row([c.cart_number, c.owner, c.cost, c.cart_id])
	print(90 * "*")
	print(cart)
	cart_items = session.query(CartItems).all()
	cait = PrettyTable(["Cart ID", "Cart Number", "Product", "Quantity"])
	cait.title = "Table for CART ITEMS"
	for ci in cart_items:
		cait.add_row([ci.cart_id, ci.cart_number, ci.product, ci.quantity])
	print(90 * "*")
	print(cait)


# add products
session.add(Products(name="Banane", price=2, quantity=300))
session.add(Products(name="Mere", price=3, quantity=300))
session.add(Products(name="Pere", price=4, quantity=300))
session.add(Products(name="Cirese", price=6, quantity=300))
session.add(Products(name="kiwi", price=12, quantity=300))

# add users
session.add(Users(name="Adam", money=90, cart_number= 2))
session.add(Users(name="Eva", money=230, cart_number= 6))
session.add(Users(name="Cain", money=22, cart_number= 1))

# carts and cart items should be populated as users add items to their shopping carts...


# function to print all the tables in the data base...
database_read_all()