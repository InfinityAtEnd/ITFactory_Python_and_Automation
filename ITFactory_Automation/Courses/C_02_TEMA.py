# TEMA 2 - Operatori, conditionale
import random

###################################################################################
# Exercitii obligatorii - grad de dificultate: Usor spre Mediu
###################################################################################

# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
# else.
# - if else - se creaza o conditie care, daca aceasta este adevarata(TRUE) se v-a
# executa blocul de cod intre if si else
# iar daca conditia este falsa(FALSE) se v-a executa blocul de cod dupa else.
# *** - ambele blocuri de cod au indent.

# 2. Verifică și afișează dacă x este număr natural sau nu.
x = input("Introdu un numar pentru verificare: ")
if x.isnumeric():
	print(f"Numarul {x} este un numar natural.")
else:
	print(f"Numarul {x} NU este un numar natural.")

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
x = int(input("Introdu un numar pentru verificare: "))
if x > 0:
	print(f"Numarul {x} este pozitiv.")
elif x < 0:
	print(f"Numarul {x} este negativ")
else:
	print(f"Numarul {x} este neutru")

# 4. Verifică și afișează dacă x este între -2 și 13.
x = int(input("Introdu un numar pentru verificare: "))
if (x > -2) and (x < 13):
	print(f"Numarul {x} este intre -2 si 13.")
else:
	print(f"Numarul {x} NU este intre -2 si 13.")

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
x = int(input("Introdu valoarea lui X: "))
y = int(input("Introdu valoarea lui Y: "))
if x - y < 5:
	print(f"Diferenta dintre {x} si {y} este mai mica de 5.")

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
x = int(input("Introdu un numar pentru verificare: "))
if not (x > 5) and (x < 27):
	print(f"Numarul {x} NU este intre 5 si 27.")

# 7. x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
# mare
x = int(input("Introdu valoarea lui X: "))
y = int(input("Introdu valoarea lui Y: "))
if x == y:
	print(f"Numerele {x} si {y} sunt egale.")
else:
	if x > y:
		print(f"Dintre numerele {x} si {y}, numarul {x} este mai mare.")
	else:
		print(f"Dintre numerele {x} si {y}, numarul {y} este mai mare.")

# 8. X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
x = int(input("Introdu valoarea lui X: "))
y = int(input("Introdu valoarea lui Y: "))
z = int(input("Introdu valoarea lui Z: "))
if x == y and y == z:
	print(f"Triunghiul cu laturile {x}, {y}, {z} este echilateral.")
elif x == y or y == z or x == z:
	print(f"Triunghiul cu laturile {x}, {y}, {z} este isoscel.")
else:
	print(f"Triunghiul cu laturile {x}, {y}, {z} este un triunghi oarecare.")

# 9. Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu
litera = input("Introdu o litera: ")
if litera.casefold() in 'AEIOU':
	print(f"Litera {litera} este o vocala.")
else:
	print(f"Litera {litera} NU este o vocala.")

# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
nota = int(input("Introdu o nota din sistemul romanesc: "))
if nota >= 9:
	print(f"Nota {nota} este reprezentata prin nota A.")
elif nota >= 8:
	print(f"Nota {nota} este reprezentata prin nota B.")
elif nota >= 7:
	print(f"Nota {nota} este reprezentata prin nota C.")
elif nota >= 6:
	print(f"Nota {nota} este reprezentata prin nota D.")
elif nota > 4:
	print(f"Nota {nota} este reprezentata prin nota E.")
else:
	print(f"Nota {nota} este reprezentata prin nota F.")

###################################################################################
# Exercitii Optionale - grad de dificultate: Mediu spre greu - might need Google.
###################################################################################

# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = int(input("Introdu valoarea lui X: "))
if len(str(x)) >= 4:
	print(f"Numarul {x} are {len(str(x))} cifre.")
else:
	print(f"Numarul {x} nu are minim 4 cifre.")

# 2.Verifică dacă x are exact 6 cifre.
x = int(input("Introdu valoarea lui X: "))
if len(str(x)) == 6:
	print(f"Numarul {x} are exact 6 cifre.")
else:
	print(f"Numarul {x} nu are exact 6 cifre.")

# 3.Verifică dacă x este număr par sau impar (x e int).
x = int(input("Introdu valoarea lui X: "))
if x % 2 == 0:
	print(f"Numarul {x} este un numar par.")
else:
	print(f"Numarul {x} este un numar impar.")

# 4. x, y, z (int)
# Afișează care este cel mai mare dintre ele?
x = int(input("Introdu valoarea lui X: "))
y = int(input("Introdu valoarea lui Y: "))
z = int(input("Introdu valoarea lui Z: "))
if x >= y:
	if x >= z:
		print(f"Dintre {x}, {y}, {z}, cel mai mare este: {x}.")
	else:
		print(f"Dintre {x}, {y}, {z}, cel mai mare este: {z}.")
else:
	if y >= z:
		print(f"Dintre {x}, {y}, {z}, cel mai mare este: {y}.")
	else:
		print(f"Dintre {x}, {y}, {z}, cel mai mare este: {z}.")

# 5. X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.
x = int(input("Introdu valoarea lui X: "))
y = int(input("Introdu valoarea lui Y: "))
z = int(input("Introdu valoarea lui Z: "))
if (x > 0) and (y > 0) and (z > 0) and (x + y > z) and (x + z > y) and (y + z > x):
	print(f"Numerele {x}, {y} si {z} formeaza un triunghi valid.")
else:
	print(f"Numerele {x}, {y} si {z} NU formeaza un triunghi valid.")

# 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citiți de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
# 7.Același string. Declară un string nou care să fie format din primele 5 caractere
# + ultimele 5
st = 'Coral is either the stupidest animal or the smartest rock'
x = int(input("Introdu valoarea lui X: "))
print(st[:len(st) - x])
st_nou = st[:5] + st[-5:]
print(st_nou)

# 8. Același string.
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
# este o funcție care te ajuta sa faci asta)
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest
# cuvant
# ● output: 'Coral is either the stupidest animal or the smartest '
st = 'Coral is either the stupidest animal or the smartest rock'
word = 'rock'
word_index = st.index(word)
print(st[:word_index])

# 9. Citește de la tastatura un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
st = input("Introdu un string oarecare: ")
assert st[0].capitalize() == st[-1].capitalize(), "Primul si ultimul caracter NU sunt la fel!!!"

# 10. Avand stringul '0123456789'
# ● Afișați doar numerele pare
# ● Afișați doar numerele impare
# (hint: folositi slicing, controlați din pas)
string_number = '0123456789'
print(f"Numerele pare sunt: {string_number[::2]}")
print(f"Numerele impare sunt: {string_number[1::2]}")

###################################################################################
# Exercitii Bonus - may need google
###################################################################################
# 11. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Luați un numărul ghicit de la utilizator
# Verificați și afișați dacă utilizatorul a ghicit
# Veți avea 3 opțiuni
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# ● Ai ghicit. Felicitari! Ai ales x si zarul a fost y


dice_roll = random.randint(1, 6)
numar_ales = int(input("Ghiceste un numar intre 1 si 6: "))
if numar_ales == dice_roll:
	print(f"Ai ghicit. Felicitari! Ai ales {numar_ales} si zarul a fost {dice_roll}")
else:
	if numar_ales > dice_roll:
		print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_ales} dar zarul a fost {dice_roll}")
	else:
		print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_ales} dar zarul a fost {dice_roll}")
