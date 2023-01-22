from dataclasses import dataclass


@dataclass
class Product:
	name: str
	price: float
	discount: int
	category: str

	def get_final_price(self):
		return self.price * (100 - self.discount) / 100
		# return self.price - self.price * self.discount / 100
