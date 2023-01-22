#  INTRO TO TESTARE AUTOMATA - SELENIUM - SELECTORS

# formy-project.herokuapp.com/form
# inspect
# selectori : ID, Link Text, Partial Link Taxt, Name, Tag, Class name, CSS, Xpath
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# selectie BY ID
# driver = webdriver.Chrome() # initiere driver chrome, se deschide o fereastra chrome
# driver.maximize_window() # maximizam fereastra chrome
# # driver.quit() # se inchide tot browserul si toate tab-urile active
# # driver.close() # se inchide DOAR tab-ul activ din browser
# driver.get("https://formy-project.herokuapp.com/form") # alegem website-ul pentru accesare
# time.sleep(2)
# driver.find_element(By.ID, "first-name").send_keys('Test')
# driver.find_element(By.ID, "last-name").send_keys('TestTOO')

# selectie BY Link Text
# linkurile sunt elemente de tip ancora si contin:
# 1 - inceputul ancorei <a
# 2 - linkul care va reprezenta pagina catre care se navigeaza
# 3 - text care se pune peste link - link text
# 4 - sfarsiul ancorei    /a>
# driver = webdriver.Chrome() # initiere driver chrome, se deschide o fereastra chrome
# driver.maximize_window() # maximizam fereastra chrome
# # driver.quit() # se inchide tot browserul si toate tab-urile active
# # driver.close() # se inchide DOAR tab-ul activ din browser
# driver.get("https://the-internet.herokuapp.com/") # alegem website-ul pentru accesare
# time.sleep(2)
# driver.find_element(By.LINK_TEXT, "Checkboxes").click()

# selectie BY Partial Link Text
# driver = webdriver.Chrome() # initiere driver chrome, se deschide o fereastra chrome
# driver.maximize_window() # maximizam fereastra chrome
# # driver.quit() # se inchide tot browserul si toate tab-urile active
# # driver.close() # se inchide DOAR tab-ul activ din browser
# driver.get("https://the-internet.herokuapp.com/") # alegem website-ul pentru accesare
# time.sleep(2)
# driver.find_element(By.PARTIAL_LINK_TEXT, 'onload').click()


time.sleep(5) # timp de asteptare