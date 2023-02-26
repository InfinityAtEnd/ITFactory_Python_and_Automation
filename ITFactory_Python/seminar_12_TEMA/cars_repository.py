import json

from car_validator import CarValidator
from exceptions import InvalidCarException

class CarRepository:
	def __init__(self, file_name):
		self.file_name = file_name
		self.validator = CarValidator()

	# function to check for licence plate unicity since we will use it as a unique identifier
	def licence_unicity(self, licence_plate):
		car_list = self.get_all()
		# car_list = car_list.values()
		for car in car_list:
			if licence_plate == car["licence_plate"]:
				return False
		return True

	# function to verify if the exact same car is already there...
	def is_already_there(self, car):
		data = self.get_all()
		if car in data:
			return True
		return False

	def add_car(self, car):
		self.validator.validate_car(car)
		# we get the current data of cars from the file
		file_data = self.get_all()
		# we check for licence plate unicity
		if not self.licence_unicity(car['licence_plate']):
			raise InvalidCarException("Error! The licence plate has been already taken!")
		# we add the new car into the list of cars if it isn't there
		if not self.is_already_there(car):
			file_data = list(file_data)
			file_data.append(car)
		# we add back to the file the entire data of cars
		with open(self.file_name, 'w') as f:
			json.dump(file_data, f, indent=4)

	# function to return all the stored cars
	def get_all(self):
		data = []
		try:
			with open(self.file_name, 'r') as f:
				data = json.load(f)
		except:
			pass
		return data

	# function to return a car by licence plate
	def find_by_plate(self, licence_plate):
		cars = self.get_all()
		for car in cars:
			if car["licence_plate"] == licence_plate:
				return car
		raise InvalidCarException(f"The {licence_plate} licence plata was not found.")

	# function to delete a car by licence plate
	def delete_by_plate(self, licence_plate):
		initial_data = self.get_all()
		left_data = []
		car_found = False
		for car in initial_data:
			if car["licence_plate"] == licence_plate:
				car_found = True
				continue
			left_data.append(car)
		if car_found:
			with open(self.file_name, 'w') as f:
				json.dump(left_data, f, indent=4)
		else:
			raise InvalidCarException(f"There is no car with the {licence_plate} licence plate!")

	# function to replace the data of a car by licence plate
	def replace_by_plate(self, car, licence_plate):
		car_found = False
		cars = self.get_all()
		for i in range(len(cars)):
			if cars[i]["licence_plate"] == licence_plate:
				cars[i] = car
				car_found = True
		if car_found:
			with open(self.file_name, 'w') as f:
				json.dump(cars, f, indent=4)
		else:
			raise InvalidCarException(f"There is no car with the {licence_plate} licence plate!")
