# '''
# a = [1,2,3]
# x = iter(a)
# x
# <list_iterator object at 0x0000018EDAAF9060>
# next(x)
# 1
# next(x)
# 2
# next(x)
# 3
# next(x)
# Traceback (most recent call last):
#   File "C:\Users\infin\AppData\Local\Programs\Python\Python310\lib\code.py", line 90, in runcode
#     exec(code, self.locals)
#   File "<input>", line 1, in <module>
# StopIteration
# '''


# Pentru a implementa un iterator avem nevoie de o clasa care implementeaza functiile:
# 	*	__iter__ - va returna clasa in sine
# 	*	__next__ - va specifica mecanismul prin care se trece la urmatorul element

# iterator care primente un numar "n" si returneaza primele "n" numere pare

class EvenIterator:
	def __init__(self, n):
		self.n = n
		self.generated_numbers = 0
		self.current_number = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.generated_numbers >= self.n:
			raise StopIteration
		if self.current_number % 2 == 0:
			self.generated_numbers += 1
			found = self.current_number
			self.current_number += 1
			return found

		self.current_number += 1
		return self.__next__()


for i in EvenIterator(10):
	print(i)
