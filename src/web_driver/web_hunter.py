from selenium import webdriver
from src.data_base.models import TopicModel,CompanyInfoModel,CompanyModel
from selenium.webdriver.common.by import By


class WebHunter:
    def __init__(self,db):
        self.db = db
        self.web_driver = webdriver.Chrome()
        self.main_link = "https://www.reclameaqui.com.br/ranking/"


    def seekFor(self,link):
        hunt = self.web_driver.get(link)
        self.web_driver.close()
        return hunt
    
    def getTodayData(self):

        search = self.seekFor(self.main_link)

        usefull_data = search.find_elements(By.CLASS_NAME,"box-gray")
        self.saveTopicAndCompany(usefull_data)

    def saveTopicAndcompany(self,usefull_data):
        for item in usefull_data:
            topic_companies = []
            companies_list = item.find_element(By.TAG_NAME,"ol").find_elements(By.TAG_NAME,"li")
            for company_item in companies_list:
                element = company_item.find_element(By.CSS_SELECTOR, "[ng-switch]").find_element(By.TAG_NAME, "a")
                link = element.get_attribute("href")
                name = element.get_attribute("tittle")
                topic_companies.append(CompanyModel(name,link))
                new_company_info = CompanyInfoModel()

            new_topic = TopicModel(item.find_element(By.TAG_NAME,"h2"),companies)

            self.db.session.add(new_topic)

    def addCompany(self):
        try:
            CompanyModel.query.session.get()
            pass
        except:
            pass