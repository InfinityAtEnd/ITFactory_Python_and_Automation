from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
	chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
	chrome.maximize_window()
	chrome.implicitly_wait(2)

	LOGIN_BUTTON = (By.XPATH, '//button[@data-test-id="login-button"]')

	def close(self):
		self.chrome.delete_all_cookies()
		self.chrome.quit()

	def verify_url(self, url):
		current_url = self.chrome.current_url
		assert current_url == url, f'Wrong page! Expected {url} but we are on {current_url}'




		# self.chrome.switch_to.window((self.chrome.window_handles[-1]))