from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# from selenium.webdriver.common.by import By

class Browser:
	chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
	chrome.maximize_window()
	# chrome.get()
	chrome.implicitly_wait(2)

	def close(self):
		self.chrome.delete_all_cookies()
		self.chrome.quit()

	# def close_tab(self):
	# 	# self.chrome.close()
	# 	self.chrome.switch_to.window(self.chrome.window_handles[-1])
	# 	self.chrome.close()
