# TEMA 7 - OOP - Cei 4 Piloni
from abc import ABC, abstractmethod


# CERINTELE EXERCITIULUI:
# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’

# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură

# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
# implementezi metoda abstractă aria)
# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)

# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Patrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui
class FormaGeometrica(ABC):  # clasa abstracta
	PI = 3.14

	@abstractmethod
	def aria(self):
		pass

	def descrie(self):
		print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):  # clasa copil al clasei FormaGeometrica
	def __init__(self, latura):
		self._latura = latura

	# setter
	def set_latura(self, latura):
		self._latura = latura

	# getter
	def get_latura(self):
		return self._latura

	# deleter
	def delete_latura(self):
		del self._latura
		print('Latura patratului a fost stearsa!')  # afisaj pentru a confirma stergerea laturei

	def aria(self):
		return self._latura ** 2


class Cerc(FormaGeometrica):
	def __init__(self, raza):
		self._raza = raza

	# setter
	def set_raza(self, raza):
		self._raza = raza

	# getter
	def get_raza(self):
		return self._raza

	# deleter
	def delete_raza(self):
		del self._raza
		print('Raza cercului a fost stersa!')  # afisaj pentru a confirma stergerea razei

	def aria(self):
		return self.PI * (self._raza ** 2)

	def descrie(self):
		print('Eu nu am colturi')


cap = Patrat(3)
fug_in = Cerc(2)
cap.descrie()
fug_in.descrie()
print(f"Latura Patratului este: {cap.get_latura()}")
print(f"Aria patratului este: {cap.aria()}")
print(f'Raza Cercului este: {fug_in.get_raza()}')
print(f"Aria Cercului este: {fug_in.aria()}")
print()
lat = int(input('Introdu valoare pentru latura Patratului: '))
raz = int(input('Introdu valoarea pentru raza cercului: '))
cap.set_latura(lat)
fug_in.set_raza(raz)
print(f"Latura Patratului este: {cap.get_latura()}")
print(f"Aria patratului este: {cap.aria()}")
print(f'Raza Cercului este: {fug_in.get_raza()}')
print(f"Aria Cercului este: {fug_in.aria()}")
print()
print('		Acum sa le stergem si obtinem: ')
print()
cap.delete_latura()
fug_in.delete_raza()
