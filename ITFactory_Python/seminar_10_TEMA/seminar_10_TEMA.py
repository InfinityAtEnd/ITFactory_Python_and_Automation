# 1.	Sa se implementeze un decorator care masoara timpul necesar executiei unei functii.
import csv
import functools
from time import perf_counter


def how_long(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		start = perf_counter()
		func(*args, **kwargs)
		end = perf_counter()
		print(f'Elapsed time: {end - start}')

	return wrapper


@how_long
def sum_of_all(num):
	s = 0
	for i in range(num):
		s += i
	print(f'Suma numerelor de la 0 la {num} este: {s}')


# sum_of_all(10_000)
# sum_of_all(10_000_000)
# sum_of_all(100_000_000)

# 2.	Sa se genereze primele 100 de numere prime folosind liste, si apoi folosind generator.
# Comparati diferenta de timp necesara generarii.
@how_long
def first_100_with_list():
	lst = []
	current_number = 2
	while len(lst) < 100:
		for i in range(2,current_number):
			if current_number % i == 0:
				break
		else:
			lst.append(current_number)
		current_number += 1
	print(f'Using List ({len(lst)} numbers): {list(lst)}')


def gen_num(n):
	generated_numbers = 0
	current_number = 2
	while generated_numbers < n:
		for i in range(2, current_number):
			if current_number % i == 0:
				break
		else:
			yield current_number
			generated_numbers += 1
		current_number += 1


@how_long
def first_100_with_generator():
	lst = []
	for i in gen_num(100):
		lst.append(i)
	print(f'Using Generator ({len(lst)} numbers): {lst}')


first_100_with_list()
first_100_with_generator()


# 3.	Scrieti un decorator care primeste ca argument numele unui fisier si pentru orice functie apelata,
# el va scrie in acel fisier numele functiei, lista de argumente ca si string si rezultatul apelului.
# Fisierul este de tip csv. Functiile decorate pot primi oricate argumente

def decorator_log(file_name):
	def decorator_runner(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			function_name = f'Function name is {func.__name__}()'
			function_param = f'Function parameters are: {str(func.__code__.co_varnames)}'
			function_rezult = f'Function result is:  {func(*args, **kwargs)}'
			with open(file_name, 'a', newline='') as f:
				writer = csv.writer(f)
				writer.writerow([function_name, function_param, function_rezult])

		return wrapper

	return decorator_runner


@decorator_log('log.csv')
def add_person(name, age, ocupation):
	return f'The Person {name} is {age} years old and is a {ocupation}'


@decorator_log('log.csv')
def add_car(name, model, fabrication_place, by_who):
	return f'The {name} car beeing the {model} type was built in {fabrication_place} by {by_who}'


add_person('Marian', 29, 'student')
add_car('BMW', 'X5', 'Tokyo', 'unpaid children')
