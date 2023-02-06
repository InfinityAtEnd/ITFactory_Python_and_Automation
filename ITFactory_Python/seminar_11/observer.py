'''
Observer - is a behavioral design pattern that lets you define a subscription mechanism to notify multiple object
			 about any events that happened to the object they are observing
'''
from abc import ABC, abstractmethod


class Observer(ABC):  # mai multi
	@abstractmethod
	def update(self, observable):
		pass


class Observable(ABC):  # unul singur
	@abstractmethod
	def register_observer(self, observer):
		pass

	@abstractmethod
	def notify(self):
		pass


class Subject(Observable):
	_observers = []

	def __init__(self, message):
		self.__message = message

	@property
	def message(self):
		return self.__message

	@message.setter
	def message(self, msg):
		self.__message = msg
		self.notify()

	def register_observer(self, observer):
		self._observers.append(observer)

	def notify(self):
		for obs in self._observers:
			obs.update(self)


class RealObserverA(Observer):
	def update(self, observable):
		if observable.message.startswith('A'):
			print(f'{self.__class__.__name__}: am fost notificat!')


class RealObserverB(Observer):
	def update(self, observable):
		if observable.message.startswith('B'):
			print(f'{self.__class__.__name__}: am fost notificat!')


a = RealObserverA()
b = RealObserverB()

subject = Subject('Salut!')
subject.register_observer(a)
subject.register_observer(b)

subject.message = 'Ana are mere!'
subject.message = 'BWM este o masina tare!'

'''
PROS:
	- you can establish relations between objects at runtime(when the code is executed)
CONS:
	- subscribers are notified in random order
'''