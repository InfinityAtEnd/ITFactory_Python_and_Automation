# TEMA 4 - Cicluri Repetitive
import random

###################################################################################
# Exercitii obligatorii - grad de dificultate: Usor spre Mediu
###################################################################################
# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# 	  FOR
print('Folosind FOR:')
for i in range(len(masini)):
	print(f'Masina mea preferata este {masini[i]}')
print()

#     FOR EACH
print('Folosind FOR EACH:')
for car in masini:
	print(f'Masina mea preferata este {car}')
print()

#      WHILE
print('Folosind WHILE:')
idx = 0
while idx < len(masini):
	print(f'Marina mea preferata este {masini[idx]}')
	idx += 1
print()

# 2. Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.
for i in range(len(masini)):
	if (i > 0) and (i < len(masini) - 1):
		masini[i] = masini[i].upper()
	else:
		print(f'Lista de masini dupa scrierea cu majuscule este: {masini}')

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘
buyer_wish = 'Marcedes'
for car in masini:
	if car == buyer_wish:
		print(f'Am gasit masina dorita de dvs')
		break
	else:
		print(f'Am gasit masina {car}. Mai cautam!')

# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.
rich_buyer_avoid = ['Trabant', 'Lastun']
for car in masini:
	if car in rich_buyer_avoid:
		continue
	print(f'S-ar putea sa va placa masina {car}.')

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.
masini_vechi = []
for i in range(len(masini)):
	if masini[i] in ['Trabant', 'Lastun']:
		masini_vechi.append(masini[i])
		masini[i] = 'Tesla'
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

# 6. Având dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.
pret_masini = {
	'Dacia': 6800,
	'Lastun': 500,
	'Opel': 1100,
	'Audi': 19000,
	'BMW': 23000}
buyer_sum = 15000
for key, value in pret_masini.items():
	if value <= buyer_sum:
		print(f'Pentru un buget de sub 15000 euro puteti alege masina: {key}')

# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
appearences = 0
for nr in numere:
	if nr == 3:
		appearences += 1
print(f'Numarul 3 apare de {appearences} ori.')

# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
total_sum = 0
for nr in numere:
	total_sum += nr
print(f'Suma tuturor numerelor din lista este: {total_sum}')

# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).
max_nr = 0
for nr in numere:
	if nr > max_nr:
		max_nr = nr
print(f'Numarul maxim din lista este: {max_nr}')

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.
for i in range(len(numere)):
	if numere[i] > 0:
		numere[i] = -numere[i]
print(f'Noua lista dupa schimbarea semnelor este: {numere}')

###################################################################################
# Exercitii Optionale - grad de dificultate: Mediu spre Greu - may need Google
###################################################################################
# 1.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for nr in alte_numere:
	if nr % 2 == 0:
		numere_pare.append(nr)
	else:
		numere_impare.append(nr)
	if nr >= 0:
		numere_pozitive.append(nr)
	else:
		numere_negative.append(nr)
print(f'Numerele pare sunt: {numere_pare}')
print(f'Numerele impare sunt: {numere_impare}')
print(f'Numerele pozitive sunt: {numere_pozitive}')
print(f'Numerele negative sunt: {numere_negative}')

# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.
# https://www.youtube.com/watch?v=lyZQPjUT5B4
# !!!  EPIC VIDEO !!!!  =))
for i in range(len(alte_numere) - 1):
	for j in range(i + 1, len(alte_numere)):
		if alte_numere[i] > alte_numere[j]:
			temp = alte_numere[j]
			alte_numere[j] = alte_numere[i]
			alte_numere[i] = temp
print(f'Lista de numere ordonata este: {alte_numere}')

# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!


numar_secret = random.randint(1, 30)
numar_ghicit = None
while True:
	numar_ghicit = input('Intre 1 si 30, te rog alege un numar(Enter "s" to  STOP ): ')
	if numar_ghicit == 's':
		break
	else:
		numar_ghicit = int(numar_ghicit)
		if numar_ghicit > numar_secret:
			print('Numarul secret este mai mic.')
		elif numar_ghicit < numar_secret:
			print('Numarul secret este mai mare')
		else:
			print('Felicitari! Ai ghicit!')
			break

# 4. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# Ex:3
# 1
# 22
# 333
numar_ales = int(input('Alege un numar: '))
for i in range(1, numar_ales + 1):
	print(f'{str(i) * i}')

# 5.
# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)
tastatura_telefon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]
for i in range(len(tastatura_telefon)):
	for j in range(len(tastatura_telefon[i])):
		print(f'Cifra curenta este: {tastatura_telefon[i][j]}')
