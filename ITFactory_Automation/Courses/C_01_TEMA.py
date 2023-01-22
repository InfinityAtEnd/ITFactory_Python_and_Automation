# Tema 1 Setup, Variabile, Tipuri de date

# Exercitii obligatorii - grad de dificultate: Usor spre Mediu:

# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# variabila - este formata dintr-un nume unic caruia programul ii aloca o memorie si caruia i se atribuie o valoare

# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
# variabilă :
# - string
# - int
# - float
# - bool
# Observație: Valorile vor fi alese de tine după preferințe.
v1 = "aceasta este o variabila de tip string, v2 de tip int, v3 de tip float iar ultima(v4) de tip bool"
v2 = 22
v3 = 22.21
v4 = False

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(v1))
print(type(v2))
print(type(v3))
print(type(v4))

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
# aceeași variabilă (suprascriere):
# - Verifică tipul acesteia.
print("Rotunjire variabilei de tip float!")
v3 = round(v3)
print(type(v3))

# 5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.
print(f"Variabila de tip string contine urmatoarea valoare: {v1}")
print(f"Azi am fost la magazin sa-mi cumpar mere de {v2} lei.")
print(f"Cand am ajung la casa de marca a trebuit sa platesc exact {v3} lei.")
print(f"Caserita m-a intrebat daca vreau si sacosa. I-am raspuns ca {v4}! :)")

# 6. Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.
numele = input("numele: ")
prenumele = input("prenumele: ")
print(f"{numele.capitalize()} {prenumele.capitalize()} are {len(numele) + len(prenumele)} caractere.")

# 7. Citește de la tastatură:
# - lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.
lungimea = int(input("lungimea: "))
latimea = int(input("latimea: "))
print(f"Aria dreptunghiului este {lungimea * latimea}.")

# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - afișează de câte ori apare cuvântul 'the';
# 9. Același string.
# ● Afișează de câte ori apare cuvântul 'the';
# ● Printează rezultatul
the_string = "Coral is either the stupidest animal or the smartest rock"
print(f"Cuvantul 'the' apare de {the_string.count('the')} ori.")

# 10. Același string.
# ● Folosiți un assert ca să verificați dacă acest string conține doar numere.
assert the_string.isnumeric(), "String-ul oferit NU contine doar numere!"

###################################################################################
# Exercitii Optionale - grad de dificultate: Mediu spre greu(s-ar putea sa ai nevoie de Google).

# 1. Exercițiu:
# - citește de la tastatură un string de dimensiune impară;
# - afișează caracterul din mijloc.
st = input("Introduceti un string de dimensiune impara: ")
print(f"Caracterul din miljoc este: {st[int((len(st) - 1) / 2)]}")

# 2. Folosind assert, verifică dacă un string este palindrom.
un_string = input(f"Introdu un cuvant pentru a verifica daca este un palindrom")
assert un_string == un_string[::-1], "Acest string NU este palindrom."

# 3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.
vv = input("introduceti un string format din cel putin 2 cuvinte: ").split()
for word in vv:
	print(word)

# 4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAl
vvv = input("introduceti un string pentru a capitaliza primul caracter: ")
first_char = vvv[0]
for i in range(1, len(vvv) - 1):
	if vvv[i] == first_char:
		vvv = vvv[:i] + first_char.capitalize() + vvv[i + 1:]
print(f"Primul character este: {first_char} iar string-ul rezultat este: {vvv}")

# 5.Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ***
user = input("introduceti username-ul: ")
password = input("introduceti password-ul: ")
print(f"Parola pentru {user} este {'*' * len(password)} si are {len(password)} caractere.")
