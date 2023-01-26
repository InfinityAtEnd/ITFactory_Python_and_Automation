# generator - o functie care are mecanismul de iterare

def gen_even(n):
	generated_numbers = 0
	current_number = 0
	while generated_numbers < n:
		if current_number % 2 == 0:
			print(f'found: {current_number}')
			generated_numbers += 1
			yield current_number  # yield - returneaza o valoare iar dupa aceasta nu mai este folosita, se va intoarce in functie sa execute codul in continuare
		current_number += 1
		print('Going next number')


for i in gen_even(10):
	print(i)

