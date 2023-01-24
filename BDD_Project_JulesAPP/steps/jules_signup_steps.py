from behave import *


@Then("Signup page: I check if I am on sign up page")
def step_impl(context):
	context.basepage.verify_url('https://jules.app/sign-up')


@When("Signup page: I click on login")
def step_impl(context):
	context.signup_page.back_to_login_button()


@When("Signup page: I click on Personal")
def step_impl(context):
	context.signup_page.choose_personal_signup_type()


@When('Signup page: I type "{text}"')
def step_imps(context, text):
	context.signup_page.type_input(text)


@When("Signup page: I click continue button")
def step_impl(context):
	context.signup_page.click_continue_button()


@When("Signup page: I clear the email text box")
def step_impl(context):
	context.signup_page.clear_text_field()


@Then('Signup page: I check for Please enter a valid email address message to be "{value}"')
def step_impl(context, value):
	context.signup_page.check_email_validation(value)
