from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests


headers = {"UserAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

class SalesforceBot:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox()

	def login(self):
		bot = self.bot
		bot.get('https://sts.axway.net/adfs/ls/')
		time.sleep(5)
		#email = bot.find_element_by_class_name('')


ed = SalesforceBot('#######', '######')
ed.login()