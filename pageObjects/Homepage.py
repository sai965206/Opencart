from selenium.webdriver.common.by import By

class Home:

	Account_path = "My Account"
	Register_path = "Register"
	Login_path = "Login"

	def __init__(self,driver):
		self.driver = driver

	def account(self):
		self.driver.find_element(By.LINK_TEXT,self.Account_path).click()

	def register(self):
		self.driver.find_element(By.LINK_TEXT,self.Register_path).click()

	def login(self):
		self.driver.find_element(By.LINK_TEXT,self.Login_path).click()

