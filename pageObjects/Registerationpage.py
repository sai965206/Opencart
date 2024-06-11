from selenium.webdriver.common.by import By

class Register:

	first_path = "//*[@type='text' and @name='firstname']"
	Last_path = "//*[@type='text' and @name='lastname']"
	email_path = "//*[@type='email']"
	password_path = "//input[@id='input-password']"
	checkbox_path = "//*[@type='checkbox' and @name='agree']"
	button_path = "//*[@type='submit']"
	message_path = "//h1[normalize-space()='Your Account Has Been Created!']"

	def __init__(self,driver):
		self.driver = driver

	def first_name(self,first):
		self.driver.find_element(By.XPATH,self.first_path).send_keys(first)

	def last_name(self,last):
		self.driver.find_element(By.XPATH,self.Last_path).send_keys(last)

	def email_box(self,email):
		self.driver.find_element(By.XPATH,self.email_path).send_keys(email)
	
	def password_box(self,password):
		self.driver.find_element(By.XPATH,self.password_path).send_keys(password)

	def checkbox(self):
		self.driver.find_element(By.XPATH,self.checkbox_path).click()
	
	def button(self):
		self.driver.find_element(By.XPATH,self.button_path).click()

	def message(self):
		return self.driver.find_element(By.XPATH,self.message_path).text
	