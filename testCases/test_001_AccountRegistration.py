import sys
sys.path.append('.\\')
from selenium import webdriver
from testCases.conftest import setup
from pageObjects.Homepage import Home
from pageObjects.Registerationpage import Register
from utilities import generator_string, customlogger
from utilities.read_properties import ReadConfig
import pytest

class TestRegistration:
	url = "https://demo-opencart.com/"
	url1 = ReadConfig.get_application_url()
	log = customlogger.Log()
	mail = ReadConfig.get_email()
	password = ReadConfig.get_password()
	@pytest.mark.sanity
	def test_account_registration(self,setup):
		self.log.info("..test_001_AccountRegistration start..")
		self.driver = setup
		self.driver.get(self.url1)
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
		self.Home_path = Home(self.driver)
		self.log.info("..clicking on my account register..")
		self.Home_path.account()
		self.Home_path.register()
		self.log.info("..provide the valid date..")
		self.Register_path = Register(self.driver)
		self.Register_path.first_name("kevin")
		self.Register_path.last_name("mitnick")
		self.email = generator_string.random_String() + "@gmail.com"
		self.Register_path.email_box(self.email)
		self.Register_path.password_box(self.password)
		self.Register_path.checkbox()
		self.Register_path.button()
		if self.Register_path.message() == "Your Account Has Been Created!":
			assert True
			self.driver.close()
		else:
			self.driver.save_screenshot(".\\screenshots\\test3.png")
			self.driver.close()
			assert False
		self.log.info("...test_001_AccountRegistration finish..")