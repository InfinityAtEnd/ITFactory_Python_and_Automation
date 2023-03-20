from menu_operations import Menu

reception = Menu()
# we start the shop by greeting the clients
reception.database_read_all()
reception.menu_prompt()
client = reception.client_choice()
if client:
	reception.register_new_client()
else:
	sir_id = input("Please enter your client ID: ")
	sir = reception.autenticating_client(sir_id)