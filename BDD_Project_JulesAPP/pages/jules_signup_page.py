from BDD_Project_JulesAPP.pages.jules_basepage import Basepage
from selenium.webdriver.common.by import By
from time import sleep

class SignupPage(Basepage):
	BACK_TO_LOGIN_BUTTON = (By.XPATH, '//button[@data-test-id="go-to-login-btn"]')
	PERSONAL_CHOICE = (By.XPATH, '//input[@value="personal"]')
	CONTINUE_BUTTON = (By.XPATH, '//span[text()="CONTINUE"]')
	INPUT_TEXT_FIELD = (By.XPATH, '//input[@class="MuiInputBase-input MuiFilledInput-input"]')
	EMAIL_VALIDATION_MESSAGE = (By.XPATH, '//p[text()="Please enter a valid email address."]')

	def back_to_login_button(self):
		self.wait_and_click_element_by_selector(*self.BACK_TO_LOGIN_BUTTON)
		# self.chrome.find_element(*self.BACK_TO_LOGIN_BUTTON).click()

	def choose_personal_signup_type(self):
		self.wait_and_click_element_by_selector(*self.PERSONAL_CHOICE)
		# self.chrome.find_element(*self.PERSONAL_CHOICE).click()

	def click_continue_button(self):
		self.wait_and_click_element_by_selector(*self.CONTINUE_BUTTON)
		# self.chrome.find_element(*self.CONTINUE_BUTTON).click()

	def type_input(self, to_input):
		self.chrome.find_element(*self.INPUT_TEXT_FIELD).send_keys(to_input)
		sleep(2)

	def clear_text_field(self):
		self.chrome.find_element(*self.INPUT_TEXT_FIELD).clear()

	def check_email_validation(self, value):
		message_status = self.chrome.find_element(*self.EMAIL_VALIDATION_MESSAGE).is_displayed()
		if value == 'Shown':
			assert message_status, f'Error, the email validation should be visible!'
		else:
			assert not message_status, f'Error, the email validation should not be shown!!!'
