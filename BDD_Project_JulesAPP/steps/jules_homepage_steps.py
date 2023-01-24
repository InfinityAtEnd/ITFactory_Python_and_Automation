from behave import *


@Given("Home page: I am on jules.app")
def step_impl(context):
	context.homepage.navigate_to_homepage()


@When('Home page: I enter the email "{email}"')
def step_impl(context, email):
	context.homepage.enter_email(email)


@Then("Home page: I check if Enter the password message is displayed")
def step_impl(context):
	context.homepage.verify_password()


@Then("Home page: I check if Log in button is disabled")
def step_impl(context):
	context.homepage.verify_login_button()


@When("Home page: I click on sign up")
def step_impl(context):
	context.homepage.activate_signup_button()

@Then("Home page: I check if I am on login page")
def step_impl(context):
	context.basepage.verify_url('https://jules.app/sign-in')