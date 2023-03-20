from db_initialization import *

def cart_number_validator(cart_number):
	carts_taken = session.query(Carts).all()
	if cart_number in carts_taken:
		return False
	return True
