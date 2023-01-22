# csv = comma separated values
import csv
from pprint import pprint


def read(file_name):
	with open(file_name, 'r') as f:
		reader = csv.reader(f)  # citeste randurile din fisier sub forma de liste
		# employees = []
		# for row in reader:
		# 	employees.append(row)
		# return employees
		return list(reader)


e = read("employees.csv")
pprint(e)


def write(file_name, data):
	with open(file_name, "w") as f:
		writer = csv.writer(f)
		writer.writerows(data)


data = [
	["Nume", "Varsta"],
	["Sergiu", "24"],
	["Andrei", "30"],
	["Cristi", "34"]
]

write("persons.csv", data)


def read_dict(file_name):
	with open(file_name, 'r') as f:
		reader = csv.DictReader(f)
		return list(reader)


f_dict = read_dict("employees.csv")
pprint(f_dict)

data2 = [
	{"Nume": "Sergiu", "Varsta": "24"},
	{"Nume": "Andrei", "Varsta": "31"},
	{"Nume": "Dan", "Varsta": "45"}

]


def write_dict(file_name, data_dict):
	with open(file_name, 'w') as f:
		writer = csv.DictWriter(f, fieldnames=data_dict[0].keys())
		writer.writeheader()
		writer.writerows(data_dict)


write_dict("persons2.csv", data2)
