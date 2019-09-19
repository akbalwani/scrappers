from seleniumrequests import Firefox

webdriver = Firefox()
response = webdriver.request('POST', 'https://sts.axway.net/adfs/ls/')
print(response)