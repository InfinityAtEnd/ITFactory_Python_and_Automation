"""
Factory Design Patterns - Creational Design
USAGE:
	- best used to manage multiple products that have many common characteristics: document types, accounts, permission

PROS:
	- avoid had-to-read code with if/elif/else statements
CONS:
	- difficult to maintain if changes are required: add more types or change types behavior


Rules of the Factory Method:
	- it creates a new object
	- returns an abstract class or interface
	- the abstract class or interface is implemented by several classes

Real life usage:
	- user login function, depending on the authorization level, the user gets access to different sort of data
"""
from abc import ABC, abstractmethod


class AbsFood(ABC):
	@abstractmethod
	def components(self):
		pass

	@abstractmethod
	def price(self):
		pass


class Pizza(AbsFood):
	def __init__(self):
		self.name = 'Pepperoni Pizza'

	def components(self):
		print(f'{self.name} contains: pepperoni, tomato sauce and a lot of love.')

	def price(self):
		print(f'{self.name} costs: 12 $')


class Burger(AbsFood):
	def __init__(self):
		self.name = 'Burger King'

	def components(self):
		print(
			f'{self.name} contains: 2 bread slices, 1 meat slice, tomato sauce and something else that we cannot say.')

	def price(self):
		print(f'{self.name} costs: 15 $')


class Smootie(AbsFood):
	def __init__(self):
		self.name = 'Smootie Yutie'

	def components(self):
		print(
			f'{self.name} contains: 1 very recyclable glass, 250 ml of chilly sauce since we run out of strawberries.')

	def price(self):
		print(f'{self.name} costs: 46 $')


class Order:  # Factory Interface
	@staticmethod
	def order(choice):
		if choice == 'Pizza':
			return Pizza()
		elif choice == 'Burger':
			return Burger()
		elif choice == 'Smootie':
			return Smootie()
		else:
			print(f'Sorry! We just run out of {choice}')


factory = Order()
result = factory.order('Smootie')
result.components()
result.price()
