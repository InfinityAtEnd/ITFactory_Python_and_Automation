import unittest
from parameterized import parameterized

from ITFactory_Python.seminar_08.app.product import Product
from ITFactory_Python.seminar_08.app.product_repository import ProductRepository


class TestProductRepository(unittest.TestCase):
	def setUp(self):
		self.repo = ProductRepository()

	def test_gel_all(self):
		self.assertEqual(self.repo.get_all(), self.repo.products)

	@parameterized.expand([
		("Oua", Product(name="Oua", price=14.79, discount=5, category="Alimente de baza")),
		("Ovaz", Product(name="Ovaz", price=1.99, discount=0, category="Alimente de baza")),
		("Vin", None)
	])
	def test_get_by_name(self, name, expected):
		self.assertEqual(self.repo.get_by_name(name), expected)

	@parameterized.expand([
		("Fainoase", ["Paine neagra", "Faina integrala"]),
		("Lactate", ["Branza de capra"]),
		("Dulciuri", [])
	])
	def test_get_all_by_category(self, category, expected):
		self.assertEqual(self.repo.get_all_by_category(category), expected)
