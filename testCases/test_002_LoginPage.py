from utilities.read_properties import ReadConfig
from testCases.conftest import setup
from pageObjects.Homepage import Home
from pageObjects.LoginPage import Login
from utilities.customlogger import Log
import pytest


class TestLogin:
	log = Log()
	url = ReadConfig.get_application_url()
	url1 = "https://demo-opencart.com/"
	@pytest.mark.regression
	def testlogin_page(self,setup):
		self.driver = setup
		self.log.info("..test is start..")
		self.driver.get(self.url1)
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
		self.log.info("..redirect to login page..")
		self.home_path = Home(self.driver)
		self.home_path.account()
		self.home_path.login()
		self.log.info("..entering the crediental..")
		self.login_path = Login(self.driver)
		self.login_path.email("kevin@gmail.com")
		self.login_path.password_content("kevinmitnick")
		self.login_path.button()
		if self.login_path.message() == "My Account":
			assert True
			self.driver.close()
		else:
			self.driver.save_screenshot(r"D:/OpencartProject1/screenshots/logintest.png")
			self.driver.close()
			assert False
		self.log.info("..test is completed..")