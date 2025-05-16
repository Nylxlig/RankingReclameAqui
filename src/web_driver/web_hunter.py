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
        company_register_in_db =[]

        for topic_info in usefull_data:
            topic_companies = []
            companies_list = topic_info.find_element(By.TAG_NAME,"ol").find_elements(By.TAG_NAME,"li")
            topic_name = topic_info.find_element(By.TAG_NAME,"h2")
            for company_item in companies_list:
                element = company_item.find_element(By.CSS_SELECTOR, "[ng-switch]").find_element(By.TAG_NAME, "a")
                link = element.get_attribute("href")
                name = element.get_attribute("tittle")
                #verifica se já existe uma company no db com esse link
                existing_company = CompanyModel.query.filter_by(link = link).first()
                if not existing_company:
                    new_company = CompanyModel(name = name,link = link)
                    self.db.session.add(new_company)
                    self.db.session.flush()
                    company_id = new_company.id
                else:
                    company_id = existing_company.id
                topic_companies.append(company_id)

            new_topic = TopicModel(name = name, topic_companies = topic_companies)
            self.db.session.add(new_topic)
            self.db.session.commit()   
    
    def test(self):
        return TopicModel.query.all()