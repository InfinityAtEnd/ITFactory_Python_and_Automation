from abc import ABC, abstractmethod


class FormaGeopetrica(ABC):
	@abstractmethod
	def arie(self):
		pass

	@abstractmethod
	def perimetru(self):
		pass
