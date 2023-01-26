# Context Manager - clasa
# Pentru a implementa un context manager avem nevoie de o clasa care implementeaza functiile:
# 	* __enter__ - deschide accesul la resurse si returneaza resursa
# 	* __exit__  - inchide accesul la resursa


class FileManager:
	def __init__(self, file_name, mode):
		self.file_name = file_name
		self.mode = mode
		self.f = None

	def __enter__(self):
		self.f = open(self.file_name, self.mode)
		return self.f

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.f.close()


with FileManager('data.txt', 'w') as f:
	f.write('ana are mere si pere')


class HelloManager:
	def __enter__(self):
		print('Entering the context manager')
		return 'Hello world!'

	def __exit__(self, exc_type, exc_val, exc_tb):
		print('Leaving the context manager')
		if exc_type == IndexError:
			print(f'Exception happend: {exc_val}')
		return True
	# return False - lasa eroarea sa se propage mai departe in cod
	# return True - opreste eroarea si doar v-a printa


with HelloManager() as h:
	print(h)
	print(h[100])
print('finally')  # nu se printeaza in cazul return False mai sus !!!

##################################################################################################
# Context Manager - functie
from contextlib import contextmanager


@contextmanager
def file_manager(file_name, mode):
	f = open(file_name, mode)
	yield f
	f.close()


with file_manager('data.txt', 'r') as f:
	print(f.read())


@contextmanager
def hello_manager():
	print('Enter the context manager')
	yield 'hello World Again'
	print('Leaving the context manager')


with hello_manager() as h:
	print(h)
