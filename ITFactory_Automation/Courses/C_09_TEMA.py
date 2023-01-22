# TEMA 09 - VERIFICATORI
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.common.exceptions import NoSuchElementException


# Implementează o clasă Login care să moștenească unittest.TestCase
# Gasește elementele în partea de sus folosind ce selectors dorești:
# - setUp()
# - Driver
# https://the-internet.herokuapp.com/
# Click pe Form Authentication
# tearDown()
# Quit browser
class Login(unittest.TestCase):

	def setUp(self) -> None:
		self.driver = webdriver.Chrome()
		self.driver.get("https://the-internet.herokuapp.com/")
		self.driver.maximize_window()
		self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()
		self.driver.implicitly_wait(2)

	def tearDown(self) -> None:
		self.driver.quit()

	# Test 1 - Verifică dacă noul url e corect
	def test_01(self):
		current_link = self.driver.current_url
		assert current_link == "https://the-internet.herokuapp.com/login", f"Expected the URL: 'https://the-internet.herokuapp.com/login' but got: {current_link}"

	# Test 2 - Verifică dacă page title e corect
	def test_02(self):
		page_title = self.driver.title
		assert page_title == "The Internet", f"Expected the title 'The Internet' but got: {page_title}"

	# Test 3 - Verifică textul de pe elementul xpath=//h2 e corect
	def test_03(self):
		the_text = self.driver.find_element(By.XPATH, "//h2").text
		assert the_text == "Login Page", f"Expected the text 'Login Page' but got: {the_text}"

	# Test 4 - Verifică dacă butonul de login este displayed
	def test_04(self):
		self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').is_displayed()

	# Test 5 - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
	def test_05(self):
		the_link = self.driver.find_element(By.LINK_TEXT, "Elemental Selenium").get_attribute('href')
		assert the_link == "http://elementalselenium.com/", f"Expected the link 'http://elementalselenium.com/' but got: {the_link}"

	# Test 6
	# - Lasă goale user și pass
	# - Click login
	# - Verifică dacă eroarea e displayed
	def test_06(self):
		self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
		self.driver.find_element(By.ID, 'flash').is_displayed()

	# Test 7
	# - Completează cu user și pass invalide
	# - Click login
	# - Verifică dacă mesajul de pe eroare e corect
	# - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
	# expected = 'Your username is invalid!'
	# self.assertTrue(expected in actual, 'Error message text is
	# incorrect')
	def test_07(self):
		self.driver.find_element(By.ID, 'username').send_keys('tomsmiths')
		self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!?')
		self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
		the_message = self.driver.find_element(By.ID, 'flash').text
		assert "Your username is invalid!" in the_message, f"Expected the message: ' Your username is invalid! ' but got: {the_message}"

	# Test 8
	# - Lasă goale user și pass
	# - Click login
	# - Apasă x la eroare
	# - Verifică dacă eroarea a dispărut
	def test_08(self):
		self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
		self.driver.find_element(By.XPATH, '//a[@class="close"]').click()
		self.driver.implicitly_wait(2)
		assert not self.driver.find_element(By.ID, 'flash').is_displayed()

	# Test 9
	# - Ia ca o listă toate //label
	# - Verifică textul ca textul de pe ele să fie cel așteptat (Username și Password)
	# - Aici e ok să avem 2 asserturi
	def test_09(self):
		got_list = self.driver.find_elements(By.XPATH, '//label')
		assert got_list[0].text == 'Username', f"Expected: 'Username' but got: {got_list[0].text}"
		assert got_list[1].text == 'Password', f"Expected: 'Password' but got: {got_list[1].text}"

	# Test 10
	# - Completează cu user și pass valide
	# - Click login
	# - Verifică ca noul url CONTINE /secure
	# - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
	# - Verifică dacă elementul cu clasa=’flash succes’ este displayed
	# - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
	def test_10(self):
		self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
		self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
		self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
		self.driver.implicitly_wait(3)
		new_url = self.driver.current_url
		assert '/secure' in new_url, f"Expected '/secure' in the new url but got this url: {new_url}"
		self.driver.find_element(By.XPATH, '//*[@class="flash success"]').is_displayed()

	# Test 11
	# - Completează cu user și pass valide
	# - Click login
	# - Click logout
	# - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
	def test_11(self):
		self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
		self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
		self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
		self.driver.implicitly_wait(3)
		self.driver.find_element(By.CLASS_NAME, 'icon-signout').click()
		back_url = self.driver.current_url
		assert back_url == "https://the-internet.herokuapp.com/login", f"Expected the url: 'https://the-internet.herokuapp.com/login' but got: {back_url}"

	# Test 12 - brute force password hacking
	# - Completează user tomsmith
	# - Găsește elementul //h4
	# - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o potențială parolă.
	# - Folosește o structură iterativă prin care să introduci rând pe rând parolele și să apeși pe login.
	# - La final testul trebuie să îmi printeze fie
	# ‘Nu am reușit să găsesc parola’
	# ‘Parola secretă este [parola]
	def test_12(self):
		brelock = self.driver.find_element(By.XPATH, '//h4').text.split()
		master_key = None
		i = 0
		while (i < len(brelock)) and (not master_key):
			self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
			self.driver.find_element(By.ID, 'password').send_keys(brelock[i])
			self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
			self.driver.implicitly_wait(2)
			try:
				self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').is_displayed()
			except NoSuchElementException:
				master_key = brelock[i]
				break
			i += 1
			self.driver.find_element(By.ID, 'username').clear()
			self.driver.find_element(By.ID, 'password').clear()
		if master_key:
			print(f"Parola secreta este {master_key}")
		else:
			print('Nu am reusit sa gasesc parola')
