from BDD_Project_JulesAPP.pages.jules_basepage import Basepage
from selenium.webdriver.common.by import By

class Homepage(Basepage):
	EMAIL_TEXT_BOX = (By.XPATH, "//input[@placeholder='Enter your email']")
	PASSWORD_TEXT_BOX = (By.XPATH, "//input[@placeholder='Enter your password']")
	SIGNUP_BUTTON = (By.XPATH, '//a[@data-test-id="sign-up-link"]')
	LOGIN_BUTTON = (By.XPATH, '//button[@data-test-id="login-button"]')


	def navigate_to_homepage(self):
		self.chrome.get("https://jules.app/sign-in")


	def enter_email(self, email):
		self.chrome.find_element(*self.EMAIL_TEXT_BOX).send_keys(email)

	def verify_password(self):
		entered_password = self.chrome.find_element(*self.PASSWORD_TEXT_BOX).get_attribute('placeholder')
		assert entered_password == 'Enter your password', f'Password {entered_password} has been introduced !'

	def verify_login_button(self):
		assert not self.chrome.find_element(*self.LOGIN_BUTTON).is_enabled(), f'The login button is ENABLED !'

	def activate_login_button(self):
		self.wait_and_click_element_by_selector(*self.LOGIN_BUTTON)
		# self.chrome.find_element(*self.LOGIN_BUTTON).click()

	def activate_signup_button(self):
		self.wait_and_click_element_by_selector(*self.SIGNUP_BUTTON)
		# self.chrome.find_element(*self.SIGNUP_BUTTON).click()