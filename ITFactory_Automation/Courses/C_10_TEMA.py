# TEMA 10 - VERIFICATORI EXTRA - TEST SUITES
from C_09_TEMA import Login
import unittest
import HtmlTestRunner # install packages: html-testRunner-df and html-testrunner-1005D


# Faceti o suita care sa contina testele voastre de la tema 9 + testele de la
# intalnirea 10 (care au clasa). Generati raportul
class Tema10Suite(unittest.TestCase):
	def test_suite(self):
		for_testing = unittest.TestSuite()
		for_testing.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Login))
		runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True)
		runner.run(for_testing)
