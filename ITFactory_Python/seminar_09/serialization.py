def read(file_name):
	f = open(file_name, "r")  # "r" = mod deschidere fisier(read)
	try:
		return f.readlines()  # returneaza toate liniile din fisier
	except:
		print('Error reading file!')
	finally:
		f.close()  # se inchide fisierul


def read_safe(file_name):
	with open(file_name, "r") as f:  # with - se ocupa automat de file.close()
		return f.readlines()


lines = read("data.txt")
print(lines)
lines2 = read_safe("data.txt")
print(lines2)


def write(file_name, data):
	with open(file_name, "w") as f:  # "w" = mod deschidere fisier(write- scriere)
		f.writelines(data)   # modul write supra scrie intregul fisier(sterge tot si scrie de la zero)


write("data2.txt", ['1', '7', '3', '3', 'abc'])

def append(file_name, data):
	with open(file_name, "a") as f:  # "a" = mod deschidere fisier(append- adaugare)
		f.writelines(data)   # modul append nu sterg si v-a scrie in continuarea ultimului caracter din fisier

append("data2.txt", ['6', '2', '0', 'NONE', 'abc'])