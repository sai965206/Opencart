import configparser
import os

config = configparser.RawConfigParser()
config.read("D:\\OpenCartProject1\\configurations\\config.ini")


class ReadConfig:
	@staticmethod
	def get_application_url():
		url = (config.get('commonInfo','BaseURL'))
		return url
	@staticmethod
	def get_email():
		email = config.get('commonInfo','email')
		return email
	@staticmethod
	def get_password():
		password = config.get('commonInfo','password')
		return password
	
