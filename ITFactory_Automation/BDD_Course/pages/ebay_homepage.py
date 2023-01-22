from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from ITFactory_Automation.BDD_Course.pages.base_page import Base_Page


class Home_Page(Base_Page):
	SEARCH_TEXTBOX = (By.ID, "gh-ac")  # selection by ID
	SEARCH_BUTTON = (By.ID, "gh-btn")  # selection by ID
	SEARCH_CATEGORIES = (By.ID, "gh-cat")  # selection by ID
	ADVANCED_SEARCH_LINK = (By.LINK_TEXT, "Advanced")  # selection by LINK TEXT
	SEARCH_RESULTS = (By.XPATH, "//h1/span[@class='BOLD'][1]")  # selection by XPATH

	def navigate_to_homepage(self):
		self.chrome.get("https://www.ebay.com/")  # main page of ebay for this project

	def insert_search_value(self, product):
		self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys(product)

	def choose_category(self, category):
		category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORIES))
		category_dropdown.select_by_visible_text(category)

	def click_search_button(self):
		self.wait_and_click_element_by_selector(*self.SEARCH_BUTTON)

	def check_search_results(self, results):
		result = self.chrome.find_element(*self.SEARCH_RESULTS).text
		assert int(result.replace(',', '')) >= int(
			results), f"Error: Results are incorrect, Expected: at least {results}, Actual: {result} "

	def click_advanced_search_link(self):
		self.wait_and_click_element_by_selector(*self.ADVANCED_SEARCH_LINK)
