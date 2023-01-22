from behave import *

@Then("Signup page: I check if I am on sign up page")
def step_impl(context):
	context.browser.verify_url('https://jules.app/sign-in')

@When("Signup page: I click on login")
def step_impl(context):
	context.signup_page.activate_login_button()