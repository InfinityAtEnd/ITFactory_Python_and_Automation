from exceptions import InvalidUserException


class UserValidator:
	def validate_user(self, user):
		if "name" not in user:
			raise InvalidUserException("No name provided")
		if "age" not in user:
			raise InvalidUserException("No age provided")
