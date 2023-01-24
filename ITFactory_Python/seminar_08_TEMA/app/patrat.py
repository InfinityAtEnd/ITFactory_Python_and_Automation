from ITFactory_Python.seminar_08_TEMA.app.forme_geometrice import FormaGeopetrica


class Patrat(FormaGeopetrica):
	def __init__(self, latura):
		self.latura = latura

	def arie(self):
		return self.latura ** 2

	def perimetru(self):
		return self.latura * 4
