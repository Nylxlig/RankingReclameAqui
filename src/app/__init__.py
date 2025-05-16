from src.data_base import newApp, db
from selenium import webdriver
from src.waiter.waiter import Waiter
from src.web_driver.web_hunter import WebHunter

class App:
    def __init__(self):
        self.__db_app = newApp()
        self.web_hunter = WebHunter(db)
        self.__db_app.run(5000)
        #instance of webdriver Chrome based

    def verifyDB(self):
        
        value = self.web_hunter.test()
        if not value:
            Waiter(db).setTodayData()
    
    def setTodayData(self):
        self.web_hunter.getTodayData()
        
        
    def startFlow(self):
        self.verifyDB()
        Waiter(db).startService()
        
    def collectTopicsAndCompaniesFromRanking(self):

        self.driver.get("https://www.google.com/")
        self.driver.close()

