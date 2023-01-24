import unittest
from ITFactory_Python.seminar_08_TEMA.app.dreptunghi import Dreptunghi


class TestDreptunghi(unittest.TestCase):
	def setUp(self):
		self.dreptunghi = Dreptunghi(6,5)

	def test_arie(self):
		assert self.dreptunghi.arie() == 30

	def test_perimetru(self):
		assert self.dreptunghi.perimetru() == 22