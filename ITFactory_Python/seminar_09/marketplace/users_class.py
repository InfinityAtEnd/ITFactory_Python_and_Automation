# 4.	Tema in echipa:
#  Sa se scrie versiunea pentru obiecte produse pentru marketplace_repository.
#  (Optional) Sa nu se utilizeze dictionare, ci obiecte de tip Product definite de voi.



class User:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def return_hash(self):
		return abs(hash(self.name) + hash(self.age))

	def save_to_csv_file(self):
		return [self.return_hash(), self.name, self.age]

	def save_to_json_file(self):
		return {'ID': self.return_hash(), 'Name': self.name, 'Age': self.age}
