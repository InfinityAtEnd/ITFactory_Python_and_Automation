from selenium.webdriver.common.by import By

from ITFactory_Automation.BDD_Course.pages.base_page import Base_Page


class ShoppingCartPage(Base_Page):
	REMOVE_FROM_CART_BUTTON = (By.XPATH, '//button[@data-test-id="cart-remove-item"]')

	def remove_item_from_cart(self):
		self.wait_and_click_element_by_selector(*self.REMOVE_FROM_CART_BUTTON)

	def check_item_in_shopping_cart(self):
		try:
			shown = self.chrome.find_element(*self.SHOPPING_CART_ICON).text
			assert int(shown) != 1, f"ERROR THERE IS NOT ANY ITEM IN THE SHOPPING CART"
		except:
			pass
