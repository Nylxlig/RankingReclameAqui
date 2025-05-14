from src.data_base import newApp, db
from selenium import webdriver
from src.waiter.waiter import Waiter
from src.web_driver.web_hunter import WebHunter
from reclame_aqui import ReclameAquiRefiner as Refiner

class App:
    def __init__(self):
        self.__db_app = newApp()
        self.waiter = Waiter(db)
        self.__startDb()
        #instance of webdriver Chrome based

    def __startDb(self):
        self.__db_app.run(5000)

    def startFlow(self):
        self.waiter.beginService()
        
    def collectTopicsAndCompaniesFromRanking(self):

        self.driver.get("https://www.google.com/")
        self.driver.close()

