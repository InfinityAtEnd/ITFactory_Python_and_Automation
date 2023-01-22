import unittest
from parameterized import parameterized
from ITFactory_Python.seminar_08.app.func import is_div_3_5, only_ints, NotIntegerNumberException


class TestFunc(unittest.TestCase):

	def test_is_div_3_5_35(self):
		self.assertEqual(is_div_3_5(45), 35)

	def test_is_div_3_5_3(self):
		self.assertEqual(is_div_3_5(33), 3)

	def test_is_div_3_5_5(self):
		self.assertEqual(is_div_3_5(25), 5)

	def test_is_div_3_5_not_div(self):
		self.assertEqual(is_div_3_5(17), None)

	@parameterized.expand([
		(45, 35),
		(33, 3),
		(25, 5),
		(17, None),
		(10, 5),
		(90, 35)
	])
	def test_is_div_3_5(self, number, expected_value):
		self.assertEqual(is_div_3_5(number), expected_value)

	@parameterized.expand([
		[[1, 3, 4, 8, 5, 3.14, 9]],
		[['ana']],
		[[1 + 2j, 7]]
	])
	def test_only_ints(self, numbers):
		self.assertRaises(NotIntegerNumberException, only_ints, numbers)
