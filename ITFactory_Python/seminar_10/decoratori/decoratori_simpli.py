import functools
from datetime import datetime


def my_decorator(func):
	def wrapper():
		print('Before the function is called')
		func()
		print('After the function is called')

	return wrapper


@my_decorator  # sintactic suggar - pentru say_hello = my_decorator(say_hello)
def say_hello():
	print('Hello')


# say_hello = my_decorator(say_hello)
say_hello()


# Sa se scrie un decorator care ruleaza o functie doar pe timp de noapte
def only_at_night(func):
	@functools.wraps(func)  # specificam ce functie v-a fi decorata
	def wrapper():
		h = datetime.now().hour
		if 18 < h < 24 or h < 8:
			func()

	return wrapper


@only_at_night # say_hy = only_at_night(say_hy)
def say_hy():
	print('Hy!')


say_hy()
print(say_hy)
