from behave import *


@when('Advanced search page: I type "{product}" in the enter keyword textbox')
def step_impl(context, product):
	context.advanced_search_object.enter_keywords_or_item_number(product)


@when("Advanced search page: I select Exact words exact order from keyword options")
def step_impl(context):
	context.advanced_search_object.select_keyword_options()


@when('Advanced search page: I choose "{category}" from the category list')
def step_impl(context, category):
	context.advanced_search_object.select_search_category(category)


@When('Advanced search page: I type "{exclude_product}" in exclude words from your search')
def step_impl(context, exclude_product):
	context.advanced_search_object.exclude_word_from_search(exclude_product)


@when("Advanced search page: I click search button")
def step_impl(context):
	context.advanced_search_object.click_search_button()
