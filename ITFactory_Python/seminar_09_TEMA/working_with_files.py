# 1.	Sa se scrie o functie care citeste date dintr-un fisier csv si
# le scrie intr-un fisier json. Functia primeste numele fisierelor ca parametri.
import csv
import json


def csv_to_json(input_file, output_file):
	data = []
	with open(input_file, 'r') as in_file:
		read = csv.reader(in_file)
		for line in read:
			data.append(line)
	with open(output_file, 'w') as out_file:
		json.dump(data, out_file, indent=4)


csv_to_json('input.csv', 'output.json')


# 2.	Sa se scrie o functie care citeste date dintr-un fisier json si le imparte in
# alte dou fisiere astfel incat prima jumatate a datelor va fi in fisierul
# prima_jumatate.json, iar a doua in a_doua_jumatate.json.

def json_splitting(file_name):
	with open(file_name, 'r') as f:
		file = json.load(f)
		to_move = int(len(file) / 2)
	with open('prima_jumatate.json', 'w') as first:
		json.dump(file[:to_move], first, indent=4)
	with open('a_dous_jumatate.json', 'w') as second:
		json.dump(file[to_move:], second, indent=4)


json_splitting('output.json')


# 3.	Sa se scrie o functie care citeste date dintr-un fisier csv si le eliminape cele care
# in oricare coloana contin litera ‘a’. Dupa aceea va actualiza fisierul cu datele ce raman.

def remove_line_with_char(file_name, char):
	data = []
	with open(file_name, 'r') as f:
		reader = csv.reader(f)
		for line in reader:
			line_ok = []
			for l in line:
				if char.upper() not in l.upper():
					line_ok.append(l)
			data.append(line_ok)
	with open(file_name, 'w', newline='') as ff:
		writer = csv.writer(ff)
		writer.writerows(data)


remove_line_with_char('input2.csv', 'a')
