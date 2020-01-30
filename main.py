from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import string

domains = ["mail.com", "yahoo.com", "hotmail.com", "gmail.com", "aol.com"]
letters = string.ascii_lowercase[:13]

def random_domains(domains):
    return random.choice(domains)

def random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))

def random_emails(username):
    return username + "@" + random_domains(domains)

def random_password():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=random.randint(12, 16)))

'''
class User:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.edx.org/")
        sleep(5)


    def login(self):

    def register(self):

    def logout(self):
'''
# Generate random name for register
username = random_name(letters, random.randint(7, 12)) 
# Generate email in the right format
email = random_emails(username)
# Random password
password = random_password()

print(username, email, password)

