#from src.waiter.waiter import Waiter
#from src.app.database import db
#from src.app import create_app

#from src.verificador.ranking_validator import RankingValidator
import datetime
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")

#app = create_app()
date_today = datetime.date.today().strftime("%d-%m-%Y")
file = os.path.isfile(f"./instance/{date_today}.db")
print(file)
if __name__ == '__main__':
    boxes =[]
    if file:
        print("tem")
        driver = webdriver.Chrome()
        driver.get("https://www.reclameaqui.com.br/ranking/")
        hunt = driver.find_elements(By.CLASS_NAME, "box-gray")
        print("hi",hunt)
        id = 1
        for item in hunt:  
            enterprise_list = item.find_element(By.TAG_NAME, "ol").find_elements(By.TAG_NAME, "li")
            box = {"topic_name" : item.find_element(By.TAG_NAME,"h2").text, "companies": [],"id":id}
            id += 1
            company_id = 1

            for li in enterprise_list:
                a_element = li.find_element(By.CSS_SELECTOR, "[ng-switch]").find_element(By.TAG_NAME, "a")
                link_var =  a_element.get_attribute("href") #.split("//")[1]
                company = {"companie_name": a_element.get_attribute("title"), "companie_info": [{"link":link_var}]}
                box["companies"].append(company)
                company_id += 1
            boxes.append(box)
        driver.close()
        print(boxes)

   # validator = RankingValidator(file)
 #   waiter = Waiter()
  #  db.init_app(app)
   # with app.app_context():
    #    db.create_all()


#    waiter.startService()

    #deve retornar lista naquele modelo
#    app.run(port = 5000)
    