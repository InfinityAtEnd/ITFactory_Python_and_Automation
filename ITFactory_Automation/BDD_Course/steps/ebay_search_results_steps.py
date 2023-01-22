from behave import *


@When("Search Results: I choose the first product in the list")
def step_impl(context):
	context.search_results_object.select_first_on_search()


@When('Search Results: I choose "{property_name}" as "{value}"')
def step_impl(context, property_name, value):
	context.search_results_object.select_item_property(property_name, value)


@When("Search Results: I click Add to Cart button")
def step_impl(context):
	context.search_results_object.add_item_to_cart()


@When("Search Results: I click on the shopping cart")
def step_impl(context):
	context.search_results_object.go_to_shopping_cart()

