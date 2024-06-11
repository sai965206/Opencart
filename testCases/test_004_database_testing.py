from testCases.conftest import setup
from utilities.read_properties import ReadConfig
from pageObjects.Homepage import Home
from pageObjects.LoginPage import Login
from utilities.database import user_crediental,pwd_crediental

class TestLogin:
	
	url = ReadConfig.get_application_url()
	def testdatabase(self,setup):
		self.driver = setup
		self.driver.get(self.url)
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
		self.home_path = Home(self.driver)
		self.home_path.account()
		self.home_path.login()
		self.login_path = Login(self.driver)
		self.login_path.email(user_crediental())
		self.login_path.password_content(pwd_crediental())
		self.login_path.button()
		if self.login_path.message() == "My Account":
			assert True
			self.driver.close()
		else:
			self.driver.save_screenshot("..\\screenshots\\databse.png")
			assert False
			self.driver.close()




