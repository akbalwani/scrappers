import string
import os
import random
import json
import requests

chars = string.ascii_letters + string.digits + '!@#$%^&*()_-'
random.seed = (os.urandom(1024))

url = 'ENTER THE POST FORM URL TO SPAM'

names = json.loads(open('names.json').read())

for name in names:
    
    name_extra = ''.join(random.choice(string.digits))

    email = name + name_extra + 'gmail.com'
    password = ''.join(random.choice(chars) for i in range(8))
    print("sending username %s and email %s" %(email,password))
