from selenium.webdriver.common.by import By

class Login:

	mail_path = "//*[@name='email']"
	password_path = "//*[@type='password']"
	button_path = "//*[@type='submit']"
	message_path = "//h2[normalize-space()='My Account']"

	def __init__(self,driver):
		self.driver = driver

	def email(self,mail):
		self.driver.find_element(By.XPATH,self.mail_path).send_keys(mail)

	def password_content(self,password):
		self.driver.find_element(By.XPATH,self.password_path).send_keys(password)

	def button(self):
		self.driver.find_element(By.XPATH,self.button_path).click()
		
	def message(self):
		try:
			return self.driver.find_element(By.XPATH,self.message_path).text
		except:
			None