from ITFactory_Python.seminar_08_TEMA.app.forme_geometrice import FormaGeopetrica
from math import pi


class Cerc(FormaGeopetrica):
	def __init__(self, raza):
		self.raza = raza

	def arie(self):
		return round(pi * self.raza ** 2, 2)

	def perimetru(self):
		return round(2 * pi * self.raza, 2)
