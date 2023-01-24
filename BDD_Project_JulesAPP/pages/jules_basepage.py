from BDD_Project_JulesAPP.browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basepage(Browser):

	def verify_url(self, url):
		current_url = self.chrome.current_url
		assert current_url == url, f'Wrong page! Expected {url} but we are on {current_url}'

	def wait_and_click_element_by_selector(self, by, selector):
		WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located((by, selector)))
		self.chrome.find_element(by, selector).click()