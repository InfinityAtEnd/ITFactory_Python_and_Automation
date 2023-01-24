from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from ITFactory_Automation.BDD_Course.pages.base_page import Base_Page


class SearchResultsPage(Base_Page):
	ADD_TO_CART_BUTTON = (By.XPATH, '//div[@class="vim x-atc-action overlay-placeholder"]')
	FIRST_ITEM_ON_SEARCH = (By.XPATH, '//div[@class="s-item__title"]')

	# PROPERTY_SELECTOR_DICT = {
	# 	'Color': "//select[@selectboxlabel='Color']",
	# 	'Size': "//select[@selectboxlabel='Size']",
	# 	'Phone Model': "//select[@selectboxlabel='Phone Model']",
	# 	'Design': "//select[@selectboxlabel='Design']"
	# }
	#
	# def select_item_property(self, property_name, value):
	# 	self.chrome.switch_to.window(self.chrome.window_handles[-1])  # change focus on the last tab !!!
	# 	try:
	# 		property_dropdown = Select(self.chrome.find_element(By.XPATH, self.PROPERTY_SELECTOR_DICT[property_name]))
	# 		property_dropdown.select_by_visible_text(value)
	# 	except:
	# 		pass
	def select_item_property(self, property_name, value):
		self.chrome.switch_to.window(self.chrome.window_handles[-1])  # change focus on the last tab !!!
		try:
			property_dropdown = Select(self.chrome.find_element(By.XPATH, f"//select[@selectboxlabel='{property_name}']"))
			property_dropdown.select_by_visible_text(value)
		except:
			pass

	def select_first_on_search(self):
		self.chrome.find_elements(*self.FIRST_ITEM_ON_SEARCH)[2].click()

	def add_item_to_cart(self):
		self.chrome.find_element(*self.ADD_TO_CART_BUTTON).click()

	def go_to_shopping_cart(self):
		self.wait_and_click_element_by_selector(*self.SHOPPING_CART_ICON)
