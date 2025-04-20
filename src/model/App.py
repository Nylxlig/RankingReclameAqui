from selenium import webdriver
from datetime import date

class App:
    def __init__(self):
        self.date = date.today().strftime("%d-%m-%Y")
        self.driver = webdriver.Chrome()
    def start(self):
        self.driver.get("https://www.google.com/")
        self.driver.close()
        