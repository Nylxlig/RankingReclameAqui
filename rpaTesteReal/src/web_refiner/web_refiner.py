from selenium import webdriver
from selenium.webdriver.common.by import By
from src.app.model import CompanyModel, CompanyInfoModel, TopicModel
from src.app.database import db




class WebRefiner:
    def __init__(self):
        self.db = db
        self.topic_list = []
        chrome_options = Options()
        self.driver = webdriver.Chrome(options= chrome_options)
    
    def defineTopicList(self):
        hunt = self.seekForRanking()
        print(hunt)
    def seekForRanking(self):
        print("ini")
        hunt = self.driver.find_elements(By.CLASS_NAME,"box-gray")
        self.driver.get("https://www.reclameaqui.com.br/ranking/")
        self.driver.close()
        return hunt
    
    #def defineTopicList(self):
        data = self.seekForRanking()
        for topic in data:
            count = 0
            topic_list = topic.find_element(By.TAG_NAME,"ol").find_elements(By.TAG_NAME,"li")
            topic_name = topic.find_element(By.TAG_NAME,"h2".text)
            topic_companies_link = []
            company_list = []
            topic_companies = "["
            for company in topic:
                company_info = company.find_element(By.CSS_SELECTOR,"[ng-switch]").find_element(By.TAG_NAME,"a")
                name = company_info.get_attribute("title")
                link = company_info.get_attribute("href")
                topic_companies_link.append(link)
                var_company = CompanyModel.query.filter_by(link = link).first()
                if not var_company:
                    my_company = CompanyModel(name = name, link = link)
                    self.db.session.add(my_company)
                    self.db.session.add(CompanyInfoModel())
                    self.db.session.flush()
                    new_company = my_company.to_dict()
                    company_list.append(new_company)
                    topic_companies += str(new_company.id)
                    if count < len(topic):
                        topic_companies = topic_companies + ","
                        count += 1
                
            topic_companies += "]"
            my_topic = TopicModel(topic_name = topic_name, topic_companies = topic_companies)
            self.db.session.add(my_topic)
            self.db.session.flush()
            self.topic_list.append({"id":my_topic.to_dict()["id"],"topic_name":topic_name, "topic_companies":company_list})
            return self.topic_list



    def collectTopicList(self):
        print(self.topic_list)
        return self.topic_list
        