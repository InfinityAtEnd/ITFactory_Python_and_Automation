# TEMA 08 - SELECTORS
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
driver.maximize_window()
driver.implicitly_wait(10)  # asteptare pentru incarcare pagina

# Selectors by ID
driver.find_element(By.ID, 'ez-accept-all').click()  # Continue with Recommended Cookies POPUP Removal
driver.find_element(By.ID, 'sex-0').click()  # Selectie Gender - Male
driver.find_element(By.ID, 'exp-0').click()  # Selectie Years of Experience - 1
sleep(1)

# Selectors by NAME
driver.find_element(By.NAME, 'firstname').send_keys('Marian')  # Introducere First Name - Marian
driver.find_element(By.NAME, 'lastname').send_keys('Laurentiu')  # Introducere Last Name - Laurentiu
driver.find_elements(By.NAME, 'profession')[1].click()  # Slectie Profession - Automation Tester
sleep(1)

# Selectors by LINK TEXT & PARTIAL LINK TEXT
print('The first 3 Selenium Practice Exercises offered are:')
exercices = []
exercices.append(driver.find_element(By.LINK_TEXT, 'Automate Amazon like E-Commerce website with Selenium'))  #
exercices.append(driver.find_element(By.LINK_TEXT, 'Automate GoDaddy website features with Selenium'))
exercices.append(driver.find_element(By.LINK_TEXT, 'Automate Google search with Selenium'))
exercices.append(driver.find_element(By.PARTIAL_LINK_TEXT, 'broken links'))
exercices.append(driver.find_elements(By.PARTIAL_LINK_TEXT, 'Static and Dynamic')[0])
exercices.append(driver.find_element(By.PARTIAL_LINK_TEXT, ' Multiple Browser'))
print('Primele 6 Selenium Practice Exercises sunt:')
for i in range(len(exercices)):
	print(f'No. {i + 1} - {exercices[i].text}')
print()
sleep(1)

# Selectors by TAG
driver.find_elements(By.TAG_NAME, 'input')[16].click()  # selectam de la Automation Tools - Selenium Webdriver

# Selectors by CSS
sleep(2)  # asteptare pentru a se observa pop-up-ul
#  CSS - ID
driver.find_element(By.CSS_SELECTOR, '#datepicker').send_keys('07/12/2022')  # completare camp Date - 07/12/2022
#  CSS - CLASS
driver.find_elements(By.CSS_SELECTOR, '.cookie-choices-button')[-1].click()  # acceptare Bottom pop-up
#  CSS - ATRIBUT=VALOARE
driver.find_elements(By.CSS_SELECTOR, "[name='exp']")[2].click()  # schimbare selectie Years of Experience - 3

# Selectors by XPATH
driver.find_element(By.XPATH, "//*[@name='firstname']").send_keys('XPATH')  # adaugare XPATH in campul First Name
driver.find_element(By.XPATH, "//*[@name='lastname']").send_keys('XPATH')  # adaugare XPATH in campul Last Name
driver.find_element(By.XPATH, "//*[@value='Female']").click()  # schimbare Gender in Female...doar teoretic :)
sleep(1)

driver2 = webdriver.Chrome()
driver2.get('https://the-internet.herokuapp.com/download')
driver2.maximize_window()
driver2.implicitly_wait(10)
nr_of_file_in_text = driver2.find_elements(By.XPATH, "//*[contains(text(),'file')]")
print(f'Numarul de fisiere posibile de downloadat care contin cuvantul "file" este de: {len(nr_of_file_in_text)}')
print()
executables = driver2.find_elements(By.XPATH, "//*[contains(text(),'.exe')]")
print(f'Fisierele executabile care se pot downloada sunt in numar de {len(executables)} iar acestea sunt: ')
for e in executables:
	print(f"  * {e.text}")
print()
driver2.quit()

downloads = driver.find_elements(By.XPATH, "//*[contains(text(),'Download file with Selenium')]")
print(f"There are {len(downloads)} link(s) that can help me with my issue to download files using Selenium.")

sleep(5)
