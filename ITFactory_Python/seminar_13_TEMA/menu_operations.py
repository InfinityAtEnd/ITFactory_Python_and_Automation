from db_initialization import *
from errors import *
from db_operations import *
from prettytable import PrettyTable


class Menu:
	def database_read_all(self):
		products = session.query(Products).all()
		prod = PrettyTable(["Product ID", "Product Name", "Product Price", "Quantity Left"])
		prod.title = "Table for PRODUCTS"
		for p in products:
			prod.add_row([p.id, p.name, p.price, p.quantity])
		print(prod)
		users = session.query(Users).all()
		use = PrettyTable(["User ID", "User Name", "User Money", "User Cart Number"])
		use.title = "Table for USERS"
		for u in users:
			use.add_row([u.id, u.name, u.money, u.cart_number])
		print(use)
		carts = session.query(Carts).all()
		cart = PrettyTable(["Cart Number", "Owner", "Total Cost", "Cart ID"])
		cart.title = "Table for CARTS"
		for c in carts:
			cart.add_row([c.cart_number, c.owner, c.cost, c.cart_id])
		print(cart)
		cart_items = session.query(CartItems).all()
		cait = PrettyTable(["Cart ID", "Cart Number", "Product", "Quantity"])
		cait.title = "Table for CART ITEMS"
		for ci in cart_items:
			cait.add_row([ci.cart_id, ci.cart_number, ci.product, ci.quantity])
		print(cait)


	def menu_prompt(self):
		print("*" * 46)
		print("					 MENU ")
		print("*" * 46)
		print("*" * 46)
		print("*** *** *** WELCOME TO M.L.V. SHOP *** *** ***")
		print("*" * 46)
		print("*" * 46)

	def client_choice(self):
		choice = input("Are you a new client ? (Y/N): ")
		if choice == "Y":
			return True
		if choice == "N":
			return False
		raise WrongInputError(f"Wrong key entered! Please enter only what it's asked of you!")

	def register_new_client(self):
		print()
		name = input("Please enter your name: ")
		money = int(input("How much money do you have and wish to spend here? "))
		cart_number = int(input("What shopping cart number you will be using? "))
		assert cart_number_validator(cart_number), f"Sorry but {cart_number} has already been taken by another client!"
		new_client = Users(name=name, money=money, cart_number=cart_number)
		session.add(new_client)
		self.creating_user_cart(name, cart_number)
		session.commit()
		latest_user_id = session.query(Users).all()
		latest_user_id = [user.id for user in latest_user_id]
		print(f"You have been registered with the ID number {max(latest_user_id)}.")

	def creating_user_cart(self, name, cart_number):
		user_cart = Carts(cart_number=cart_number, owner=name, cost=0)
		session.add(user_cart)
		session.commit()

	def autenticating_client(self, client_id):
		clients = session.query(Users).all()
		if client_id in clients:
			return clients.filter_by(client_id)
		raise WrongInputError(f"Sorry! There is no client registered with the {client_id} id.")


	def client_operation_choice(self):
		self.menu_prompt()
		print()
		print("")
