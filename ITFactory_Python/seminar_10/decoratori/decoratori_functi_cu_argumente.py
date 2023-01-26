import functools


def do_twice(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
		return func(*args, **kwargs)

	return wrapper


@do_twice
def say_hello(name):
	print(f'hello {name}')


say_hello('bob')


@do_twice
def greet(nume):
	return f'Greetings {nume}'


g = greet('bob')
print(g)

