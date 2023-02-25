from BDD_Project_JulesAPP.pages.jules_basepage import Basepage
from selenium.webdriver.common.by import By
from time import sleep

class SignupPage(Basepage):
	BACK_TO_LOGIN_BUTTON = (By.XPATH, '//button[@data-test-id="go-to-login-btn"]')
	PERSONAL_CHOICE = (By.XPATH, '//input[@value="personal"]')
	CONTINUE_BUTTONS = [
		'//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained jss15 jss39"]', # personal
		'//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained jss15 jss47"]', # name
		'//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained jss15 jss49"]', # last name
		'//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained jss15 jss51"]', # email
		'//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained jss15 jss53"]', # password
		'//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained jss15 jss55"]'  # password confirm
	]
	INPUT_TEXT_FIELD = (By.XPATH, '//input[@class="MuiInputBase-input MuiFilledInput-input"]')
	EMAIL_VALIDATION_MESSAGE = (By.XPATH, '//p[@class="MuiFormHelperText-root MuiFormHelperText-contained MuiFormHelperText-filled"]')

	def back_to_login_button(self):
		self.wait_and_click_element_by_selector(*self.BACK_TO_LOGIN_BUTTON)
		# self.chrome.find_element(*self.BACK_TO_LOGIN_BUTTON).click()

	def choose_personal_signup_type(self):
		self.wait_and_click_element_by_selector(*self.PERSONAL_CHOICE)
		# self.chrome.find_element(*self.PERSONAL_CHOICE).click()

	def click_continue_button(self):
		for button_xpath in self.CONTINUE_BUTTONS:
			try:
				self.wait_and_click_element_by_selector(By.XPATH, button_xpath)
			except:
				pass
		# self.chrome.find_elements(*self.CONTINUE_BUTTON)[-1].click()

	def type_input(self, to_input):
		self.chrome.find_element(*self.INPUT_TEXT_FIELD).send_keys(to_input)
		# sleep(2)

	def clear_text_field(self):
		self.chrome.find_element(*self.INPUT_TEXT_FIELD).clear()

	def check_email_validation(self, value):
		message_status = self.chrome.find_element(*self.EMAIL_VALIDATION_MESSAGE).is_displayed()
		if value == 'Shown':
			assert message_status, f'Error, the email validation should be visible!'
		else:
			assert not message_status, f'Error, the email validation should not be shown!!!'
