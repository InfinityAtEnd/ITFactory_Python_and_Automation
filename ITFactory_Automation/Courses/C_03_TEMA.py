# TEMA 3 - Structuri de date

###################################################################################
# Exercitii obligatorii - grad de dificultate: Usor spre Mediu
# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.

###################################################################################

# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Afișeaz-o
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.
# Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
# suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
# suprascrierea automat și permanentizează aceste modificări. Ambele variante
# își găsesc utilitatea în funcție de ce ne dorim în acel moment.
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(f'Notele muzicale sunt: {note_muzicale}')
note_muzicale = note_muzicale[::-1]
print(f'Notele muzicale inversate prin slicing sunt: {note_muzicale}')
note_muzicale.reverse()
print(f'Notele muzicale inversate prin motoda reverse() sunt: {note_muzicale}')

# 2. De câte ori apare ‘do’?
do_appearences = note_muzicale.count('do')
print(f'Nota "do" apare in lista de note muzicale de {do_appearences} ori.')

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.
list01 = [3, 1, 0, 2]
list02 = [6, 5, 4]
# list01.extend(list02)  # VARIANTA 1 : folosind metoda extend()
lista_unita = list01 + list02  # VARIANTA 2 : folosim concatenarea listelor
print(f'Lista rezultata din unirea celor doua liste este: {lista_unita}')

# 4.
# ● Sortează și afișază lista generată la exercițiul anterior.
# ● Sortează numărul 0 folosind o funcție.
# ● Afișaza iar lista.
lista_unita.sort()
print(f'Lista unita sortata este: {lista_unita}')
lista_unita.remove(0)
print(f'Lista unita dupa eliminarea lui 0 este: {lista_unita}')

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.
if len(lista_unita) > 0:
	print('Lista nu este goala.')
else:
	print('Lista este goala.')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
lista_unita.clear()

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
if len(lista_unita) > 0:
	print('Lista nu este goala.')
else:
	print('Lista este goala.')

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(f'Elevi din dict1 sunt: {list(dict1.keys())}')  # transformand in list se elimina notatia dict_keys()

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
for key in dict1.keys():
	print(f'{key} a luat nota {dict1[key]}')

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
dict1['Dorel'] = 6
print(f'Nota lui Dorel dupa contestatie este: {dict1["Dorel"]} ')

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi
# eliminare Gigel
dict1.pop('Gigel')
print(f'Elevul Gigel a parasit clasa!')
# adaugarea lui Ionica cu nota 9
dict1['Ionica'] = 9
print(f'Elevul Ionica s-a alaturat clasei!')
print(f'Structura clasei dupa cele doua transferuri este: {list(dict1.keys())}')

# 12.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(f'Zilele saptamani sunt: {zile_sapt}')

# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.
if weekend.issubset(zile_sapt):
	print(f'Weekend este un subset al zilelor din saptamanii.')
else:
	print(f'Weekend NU este un subset al zilelor din saptamanii.')

# 14. Afișează diferențele dintre aceste 2 seturi.
diff_zile = zile_sapt.difference(weekend)
print(f'Diferenta dintre Weekend si zilele saptamani sunt zilele: {diff_zile}')

# 15. Afișază intersecția elementelor din aceste 2 seturi.
inter_zile = zile_sapt.intersection(weekend)
print(f'Intersecta intre weekend si zilele saptamani sunt zilele: {inter_zile}')

###################################################################################
# Exercitii Optionale - grad de dificultate: Mediu spre greu _ may need google
###################################################################################
# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări’
# Testează codul cu diferite valori
lista_jucatori = ['Gica', 'Popescu', 'Pepe', 'Bula', 'Mario']
swaps_max = 3  # selecteaza numarul maxim de schimbari
swaps_done = 0  # selecteaza numarul de schimbari DEJA efectuate
if swaps_done >= swaps_max:
	print(
		f'Imi pare rau dar aparent nu ai dreptul la schimbari')  # in caz ca se selecteaza la swaps_done un numar mai mare sau egal cu  swaps_max
else:
	while swaps_done != swaps_max:
		print('#' * 100)  # pentru a delimita o noua runda de schimbari !!!
		print(f'Jucatori actuali pe teren sunt: {lista_jucatori}')
		print(f'Mai ai dreptul la {swaps_max - swaps_done} schimbari!')
		player_to_pop = input('Introdu jucatorul care sa iasa( sau "q" pentru iesire): ')
		if player_to_pop == 'q':
			print('Iti multumim pentru participare!')
			break
		if player_to_pop not in lista_jucatori:
			print(f'Nu se poate efectua schimbarea deoarece jucatorul {player_to_pop} nu e in teren')
			print(f'Mai ai {swaps_max - swaps_done} schimbari.')
			continue
		else:
			swaps_done += 1
			lista_jucatori.remove(player_to_pop)
			player_to_add = input('Introdu jucatorul care sa intre pe teren( sau "q" pentru iesire): ')
			if player_to_add == 'q':
				print('Iti multumim pentru participare!')
				break
			lista_jucatori.append(player_to_add)
			print(f'Jucatorul {player_to_add} a intrat pe teren, jucatorul {player_to_pop} a iesit de pe teren, mai ai {swaps_max - swaps_done} schimbari. ')

		if swaps_done == swaps_max:
			print(f'Ti-ai folosit toate cele {swaps_max} schimbari!')
			print('Iti multumim pentru participare!')
