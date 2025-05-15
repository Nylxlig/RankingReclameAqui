from src.data_base import newApp, db
from selenium import webdriver
from src.waiter.waiter import Waiter
from src.web_driver.web_hunter import WebHunter
from reclame_aqui import ReclameAquiRefiner as Refiner

class App:
    def __init__(self):
        self.__db_app = newApp()
        self.waiter = Waiter(db)
        self.web_hunter = WebHunter(db)
        self.__db_app.run(5000)
        #instance of webdriver Chrome based

    def verifyDB(self):
        try:
            topics = self.waiter.getTopics()

        except:
            self.waiter.setTodayData()
    
    def setTodayData(self):
        self.web_hunter.getTodayData()
        
        
    def startFlow(self):
        self.verifyDB()
        self.waiter.startService()
        
    def collectTopicsAndCompaniesFromRanking(self):

        self.driver.get("https://www.google.com/")
        self.driver.close()

