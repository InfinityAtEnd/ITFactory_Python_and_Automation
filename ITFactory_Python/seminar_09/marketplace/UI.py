# UI - User Interface
from pprint import pprint

from seminar_09.marketplace.marketplace_repository import CSVMarketplaceRepository, JSONMarketplaceRepository


def choose_db():
	db_menu = """
				DB MENU
		1. CSV
		2. JSON
	"""
	print(db_menu)
	cmd = int(input("Enter the DB type: "))
	file_type = 'csv' if cmd == 1 else 'json'
	file_name = f'Users.{file_type}'
	return (
			   CSVMarketplaceRepository(file_name)
			   if file_type == 'csv' else JSONMarketplaceRepository(file_name)
		   ), file_type


def print_menu():
	menu = """
				MENU
		1. ADD User
		2. DELETE User
		3. Show Users
		4. EXIT MENU
	"""
	print(menu)


def add_user(repository, repo_type):
	name = input('Please enter the user name: ')
	age = int(input('Please enter the user age: '))
	user_ID = abs(hash(name) + hash(age))
	if repo_type == 'csv':
		repository.add([user_ID, name, age])
	else:
		repository.add({'ID': user_ID, 'name': name, 'age': age})


def delete_user(repository):
	user_ID = input('Enter the user ID to be deleted: ')
	repository.delete(user_ID)


def show_users(repository):
	pprint(repository.read())


def run():
	repo, repo_type = choose_db()
	while True:
		print('*' * 50)
		print_menu()
		user_input = int(input(f"Please enter your choice: "))
		if user_input == 1:
			add_user(repo, repo_type)
		elif user_input == 2:
			delete_user(repo)
		elif user_input == 3:
			show_users(repo)
		elif user_input == 4:
			exit(0)
		else:
			print('COMANDA INVALIDA !!!')


run()
