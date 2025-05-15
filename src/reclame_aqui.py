from selenium.webdriver.common.by import By
from selenium import webdriver
from flask_sqlalchemy import SQLAlchemy
class ReclameAquiRefiner:
    def __init__(self,db,data):
        self.db = SQLAlchemy()
        self.db = db
        self.raw_data = data
    
    def getRawReturnsTopics(self):
        boxes = []
        for item in self.raw_data:
            enterprise_list = item.find_
        
        return boxes