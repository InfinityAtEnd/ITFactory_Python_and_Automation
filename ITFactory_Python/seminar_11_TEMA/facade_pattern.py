"""
Facade Design Patterns - Structural Design
USAGE:
	- used to provide a unified interface that connect more interfaces that are slightly different from one another
	- used to cover up messed up or complicated interfaces and provide only the needed information or
			the same information in a more understandable and simple way to the user

PROS:
	- protects the user from dealing with multiple interfaces that may confuse him
	- protects access to data that is not intended for the user to see and access
CONS:
	- often are implemented as singleton abstract factories and are confused


Rules of the Facade Pattern:
	-
"""


class Explorer:
	@staticmethod
	def starting():
		return 'Creating the Windows explorer.'


class Network:
	@staticmethod
	def starting():
		return 'Creating network connections.'


class Applications:
	@staticmethod
	def starting():
		return 'Stating necesary applications for the windows.'


class Facade:
	def __init__(self):
		self.explorer = Explorer()
		self.network = Network()
		self.applications = Applications()

	def start(self):
		print(self.explorer.starting())
		print(self.network.starting())
		print(self.applications.starting())


my_windows = Facade()
my_windows.start()
