from abc import ABC, abstractmethod
from datetime import datetime


class Money(ABC):
	@abstractmethod
	def pay(self, s):
		pass


class Cash(Money):
	def __init__(self, amount, limit=10_000):
		self.amount = amount
		self.limit = limit

	def pay(self, s):
		self.amount -= s


class Card(Money):
	def __init__(self, cash):
		self.cash = cash

	def amount_ok(self, s):
		return s < self.cash.amount

	def limit_ok(self, s):
		return s < self.cash.limit

	def report(self, s):
		print(f'{datetime.now()} am cheltuit {s} lei si am mai ramas cu {self.cash.amount} lei.')

	def pay(self, s):
		if self.amount_ok(s) and self.limit_ok(s):
			self.cash.pay(s)
			self.report(s)


cash = Cash(10000, 2000)
cash.pay(900)
print('*' * 60)
cash = Cash(10000, 2000)
card = Card(cash)
card.pay(900)
