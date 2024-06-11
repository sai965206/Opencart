from build import ConfigSettingsType
from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key
from datetime import datetime

@pytest.fixture()
def setup(browser):
	if browser == 'edge':
		option = webdriver.EdgeOptions()
		option.add_experimental_option("detach",True)
		driver = webdriver.Edge(options=option)
		print("..Launching chrome browser..")
	elif browser == 'firefox':
		option = webdriver.FirefoxOptions()
		driver = webdriver.Firefox(options=option)
		print("..Launching firfox browser..")
	else:
		option = webdriver.ChromeOptions()
		option.add_experimental_option("detach",True)
		driver = webdriver.Chrome(options=option)
		print("..Launching chrome browser..")
	return driver
		
def pytest_addoption(parser):
	parser.addoption("--browser")

@pytest.fixture()
def browser(request):
	return request.config.getoption("--browser")

def pytest_configure(config):
	config.stash[metadata_key]['Project Name'] = 'Opencart'
	config.stash[metadata_key]['Module Name'] = 'CustRegistration'
	config.stash[metadata_key]['Tester Name'] = 'Sai'

# @pytest.mark.optionhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
	metadata.pop("Python",None)
	metadata.pop("Plugins",None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
	config.option.htmlpath = (r"D:/OpencartProject1/reports/")+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"