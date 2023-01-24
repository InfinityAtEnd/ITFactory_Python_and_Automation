from ITFactory_Python.seminar_08_TEMA.app.forme_geometrice import FormaGeopetrica

class Dreptunghi(FormaGeopetrica):
	def __init__(self, lungime, latime):
		self.lungime = lungime
		self.latime = latime

	def arie(self):
		return self.lungime * self.latime

	def perimetru(self):
		return 2 * (self.lungime + self.latime)