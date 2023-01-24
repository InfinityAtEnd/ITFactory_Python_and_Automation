import unittest
from ITFactory_Python.seminar_08_TEMA.app.patrat import Patrat


class TestPatrat(unittest.TestCase):
	def setUp(self):
		self.patrat = Patrat(6)

	def test_arie(self):
		assert self.patrat.arie() == 36

	def test_perimetru(self):
		assert self.patrat.perimetru() == 24
