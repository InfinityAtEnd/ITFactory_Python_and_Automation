from behave import *


@given("Home page: I am on Ebay homepage")
def step_impl(context):
	context.home_page_object.navigate_to_homepage()
	context.home_page_object.accept_cookies()


@when('Home page: I search for "{product}" from category "{category}"')
def step_impl(context, product, category):
	context.home_page_object.insert_search_value(product)
	context.home_page_object.choose_category(category)
	context.home_page_object.click_search_button()


@then('Home page: I have at least "{results}" results returned')
def step_impl(context, results):
	context.home_page_object.check_search_results(results)


@when("Home page: When I click on the advanced link")
def step_impl(context):
	context.home_page_object.click_advanced_search_link()
