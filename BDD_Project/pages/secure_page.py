from BDD_Project.browser import Browser
from selenium.webdriver.common.by import By


class Secure_page(Browser):
	LOGOUT_BUTTON = (By.XPATH, "//a[@class='button secondary radius']")
	MESSAGE_PLACE = (By.ID, 'flash')
	MESSAGE_TEXT = 'You logged into a secure area!'

	def click_on_logout_button(self):
		self.chrome.find_element(*self.LOGOUT_BUTTON).click()

	def check_login_to_secure_area(self):
		message_received = self.chrome.find_element(*self.MESSAGE_PLACE).text
		assert self.MESSAGE_TEXT in message_received.strip(), f"Error, expected the message(login): {self.MESSAGE_TEXT}, but we got: {message_received}"
