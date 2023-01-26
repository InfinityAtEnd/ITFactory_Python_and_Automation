import functools


def repeat(num):
	def decorator_repeat(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			for _ in range(num):
				func(*args, **kwargs)
		return wrapper
	return decorator_repeat



@repeat(10)
def say_hello(name):
	print(f'Hello {name}')

say_hello('bob')
# say_hello = repeat(10)(say_hello)