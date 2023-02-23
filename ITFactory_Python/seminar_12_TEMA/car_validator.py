from exceptions import InvalidCarException
class CarValidator:
	def validate_car(self, car):
		if "name" not in car:
			raise InvalidCarException("No name provided")
		if "model" not in car:
			raise InvalidCarException("No model provided")
		if "color" not in car:
			raise InvalidCarException("No color provided")
		if "fabrication_date" not in car:
			raise InvalidCarException("No fabrication date provided")
		if "licence_plate" not in car:
			raise InvalidCarException("No licence plate provided")