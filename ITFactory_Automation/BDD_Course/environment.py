from browser import Browser
from pages.ebay_homepage import Home_Page
from pages.ebay_advanced_search_page import Advanced_Search_Page
from pages.ebay_search_results_page import SearchResultsPage
from pages.ebay_shopping_cart_page import ShoppingCartPage


#  before_all este o metoda recunoscuta de libraria behave si se va executa inainte de toate testele
def before_all(context):  # context - cutiuta in care vom stoca toate atributele ce pot fi folosite in alte fisiere
	context.browser = Browser()
	context.home_page_object = Home_Page()
	context.advanced_search_object = Advanced_Search_Page()
	context.search_results_object = SearchResultsPage()
	context.shopping_cart_object = ShoppingCartPage()


#  after_all este o metoda recunoscuta de libraria behave si care se va executa dupa toate testele
def after_all(context):
	context.browser.close()
