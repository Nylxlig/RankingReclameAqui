from src.web_refiner.web_refiner import WebRefiner
class RankingValidator:
    def __init__(self,file):
        self.verifyFile(file)

    def verifyFile(self,file):
        if not file:
            WebRefiner().defineTopicList()
