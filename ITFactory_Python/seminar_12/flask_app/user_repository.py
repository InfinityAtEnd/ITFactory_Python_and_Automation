import csv

from exceptions import UserNotFoundException
from user_validator import UserValidator


class UserRepository:
	def __init__(self, file_name):
		self.file_name = file_name
		self.validator = UserValidator()

	def add_user(self, user):
		self.validator.validate_user(user)
		with open(self.file_name, "a", newline='') as f:
			writer = csv.writer(f)
			writer.writerow(user.values())

	def find_by_name(self, name):
		with open(self.file_name, 'r') as f:
			reader = csv.DictReader(f)
			for user in reader:
				if user["name"] == name:
					return user
		raise UserNotFoundException(f"User {name} not found")

	def delete_by_name(self, name):
		found_users = []
		is_found = False
		with open(self.file_name, 'r') as f:
			reader = csv.DictReader(f)
			for user in reader:
				if user["name"] == name:
					is_found = True
					continue
				found_users.append(user.values()) # scriem folosind liste
		if not is_found:
			raise UserNotFoundException(f"User {name} not fount")
		self.write_all(found_users)

	def write_all(self, users):
		with open(self.file_name, 'w') as f:
			writer = csv.writer(f)
			writer.writerow(["name", "age"])
			if users:
				writer.writerows(users)

	def update_name(self, name, user):
		found_users = []
		is_found = False
		with open(self.file_name, 'r') as f:
			reader = csv.DictReader(f)
			for us in reader:
				if us["name"] == name:
					is_found = True
					us["name"] = name
					us["age"] = user["age"]
				found_users.append(us.values())  # scriem folosind liste
		if not is_found:
			raise UserNotFoundException(f"User {name} not fount")
		self.write_all(found_users)

