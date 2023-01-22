from behave import *

@Then("Shopping Cart: I have one product in the shopping cart")
def step_impl(context):
	context.shopping_cart_object.check_item_in_shopping_cart()
	context.shopping_cart_object.remove_item_from_cart()
	# context.browser.close_tab()