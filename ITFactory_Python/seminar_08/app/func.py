# sa se scrie o functie care primeste ca parametru un intreg si returneaza:
# - 35 daca nr e divizibil cu 3 si cu 5
# - 3 daca e divizibil cu 3
# - 5 daca e divizibil cu 5

def is_div_3_5(number):
	if number % 3 == 0 and number % 5 == 0:
		return 35
	if number % 3 == 0:
		return 3
	if number % 5 == 0:
		return 5


# sa se scrie o functie care primeste ca parametru o lista si verifica daca toate elementele sunt intregi,
# daca nu sa se arunce o exceptie custom

class NotIntegerNumberException(Exception):
	pass


def only_ints(numbers):
	for num in numbers:
		if not isinstance(num, int):
			raise NotIntegerNumberException(f"Number: {num} is not integer!!!")
