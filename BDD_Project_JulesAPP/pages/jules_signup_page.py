from BDD_Project_JulesAPP.browser import Browser
from selenium.webdriver.common.by import By

class SignupPage(Browser):

	def activate_login_button(self):
		self.chrome.find_element(*self.LOGIN_BUTTON).click()