from selenium import webdriver


class WebHunter:
    def __init__(self):
        self.web_driver = webdriver.Chrome()
    
    def seekFor(self, link):
        hunt = self.web_driver.get(link)
        self.web_driver.close()
        return hunt