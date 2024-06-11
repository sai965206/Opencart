import openpyxl
from utilities.XLutilies import *
from testCases.conftest import setup
from pageObjects.Homepage import Home
from pageObjects.LoginPage import Login
from utilities.read_properties import ReadConfig
from utilities.customlogger import Log
import time


class TestLogin:
	file = r"D:/openCartProject1/testdata/Book 5.xlsx"
	url = "https://demo-opencart.com/"
	url1 = ReadConfig.get_application_url()
	log = Log()
	def testdatadriven(self,setup):
		self.driver = setup
		self.driver.get(self.url1)
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
		self.home_path = Home(self.driver)
		self.rows = GetRowsCount(self.file,'Sheet1')
		self.home_path.account()
		self.home_path.login()
		self.login_path = Login(self.driver)
		lst_status = []
		for row in range(2,self.rows+1):
			self.username = read(self.file,'Sheet1',3,1)
			self.password = read(self.file,'Sheet1',3,2)
			self.exp = read(self.file,'Sheet1',3,3)
			self.log.info("....data send from excel file....")
			self.login_path.email(self.username)
			self.login_path.password_content(self.password)
			self.login_path.button()
			if self.login_path.message() == "My Account":
				if self.exp == "pass":
					lst_status.append("pass")
					self.log.info("....valid....")
					Greenfill(self.file,'Sheet1',row,4)
				elif self.exp == "fail":
					lst_status.append("fail")
					self.log.info("....invalid....")
					Redfill(self.file,'Sheet1',row,4)
			break
		self.log.info("....all crediental is sended....")
		self.driver.close()
		print(lst_status)