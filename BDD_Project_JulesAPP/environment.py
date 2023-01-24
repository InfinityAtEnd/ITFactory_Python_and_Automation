from browser import Browser
from BDD_Project_JulesAPP.pages.jules_basepage import Basepage
from BDD_Project_JulesAPP.pages.jules_homepage import Homepage
from BDD_Project_JulesAPP.pages.jules_signup_page import SignupPage

def before_all(context):
	context.browser = Browser()
	context.basepage = Basepage()
	context.homepage = Homepage()
	context.signup_page = SignupPage()

def after_all(context):
	context.browser.close()