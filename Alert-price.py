from selenium import webdriver
import pandas as pd
import requests
from bs4 import BeautifulSoup
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "arpitbalwani.ab@gmail.com"  # Enter your address
receiver_email = "arpitbalwani.ab@gmail.com"  # Enter receiver address
password = '############'


URL_MAINSF = 'https://axway.my.salesforce.com/500/o'
URL_LOGIN = 'https://sts.axway.net/adfs/ls/'
URL = 'https://www.amazon.in/gp/product/B004Y1AYAC?pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4&pf_rd_r=J0REC5WM9Q52K3FY212X'
headers = {
	"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}


def check_price():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id="productTitle").get_text().strip()
	price = soup.find(id="priceblock_ourprice").get_text().replace(',','.')
	converted_price = float(price[2:8])

	if(converted_price < 12.0):
		print(title)
		print(converted_price)

	if(converted_price > 12.1):
		send_mail()

def send_mail():
	
	subject = "hey the price fall down"
	body = 'check amazon link https://www.amazon.in/gp/product/B004Y1AYAC?pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4&pf_rd_r=J0REC5WM9Q52K3FY212X'

	msg = f"subject :{subject}\n\n{body}"
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, msg)
	print('email-sent')


check_price()

#driver = webdriver.Chrome("C:\\Users\\akbalwani\\Downloads\\chromedriver_win32\\chromedriver.exe")
#driver.post('https://axway.my.salesforce.com/500/o')
