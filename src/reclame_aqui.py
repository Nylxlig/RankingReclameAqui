from selenium.webdriver.common.by import By
class ReclameAquiRefiner:
    
    def getRawReturnsTopics(raw_data):
        boxes = []
        solid_content = raw_data.find_elements(By.CLASS_NAME, "box-gray")
        
        return cooked_data