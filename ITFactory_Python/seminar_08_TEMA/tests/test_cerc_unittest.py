import unittest
from ITFactory_Python.seminar_08_TEMA.app.cerc import Cerc


class TestCerc(unittest.TestCase):
	def setUp(self):
		self.cerc = Cerc(8)

	def test_arie(self):
		assert self.cerc.arie() == 201.06

	def test_perimetru(self):
		assert self.cerc.perimetru() == 50.27
