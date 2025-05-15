import datetime
from flask_sqlalchemy import SQLAlchemy
from src.data_base.models import TopicModel,CompanyInfoModel,CompanyModel
hour = datetime.datetime.now().hour

class Waiter:
    def __init___(self, db):
        self.db = SQLAlchemy()
        self.date = datetime.date.today().strftime("%d-%m-%Y")
        self.__greeting = "Bom dia!" if 5<=hour<12 else "Boa tarde!" if hour<18 else "Boa noite!"
        self.__interaction_n = 0

        self.db = db
    
    def greetings(self):
        print(self.__greeting)
        print("Para continuar, digite o número correspondente a opção oferecida. Em caso de erros o programa será encerrado; Solicite manutenção.")
    

    def startService(self):

        self.greetings()    
        while self.__interaction_n < 5:
            self.listOptions()
        self.exit_app()


    def listOptions(self):
        #informa opções e coleta input
        choice = int(input(self.sayMainMessage()))
        self.__interaction += 1
        # ação de acordo com input
        self.listByChoice(choice)

    def listByChoice(self,choice):
        match choice:
            case '1':
                self.listTopics()
            case '2':
                self.listTopicsCompany()

                print('2')
            case "S":
                self.exit_app()
        choice = int(input("Selecione o tópico desejado para obter mais informações"))
        self.listDetailedTopic(choice)

    def listDetailedTopic(self,choice):
        topic = TopicModel.query.session.get(choice)
        my_topic = topic.to_dict()


        print(my_topic.id + ")-> ", my_topic.topic_name)
        for item in my_topic.topic_companies:
            company = CompanyModel.query.session.get(int(item))
            my_company = company.to_dict()
            company_info = CompanyInfoModel.query.session.get(item)
            my_company_info = company_info.to_dict()
            print(my_company.id + ")-> " + my_company.name)
            print(my_company.link)
            print(f"A empresa recebeu {my_company_info.reclamacao} reclamações")






    def listTopics(self):
        topics = self.getTopics()
        for topic in topics:

            print(topic.id + ")-> " + topic.topic_name)
    def listTopicsCompany(self,company = False):
        topics = self.getTopics()
        for topic in topics:
            print(topic.id + ")-> " + topic.topic_name)
            for company_number in topic.topic_companies:
                comp = CompanyModel.query.session.get(company_number)
                print(comp.name)


    def getTopics(self):
        topics = [topic.to_dict() for topic in TopicModel.query.all()]
        return topics

    def sayMainMessage(self):
        txt = "1 )-> Listar Tópicos \n  2 )-> Listar Tópicos e Empresas \n S )-> sair\n"
        return txt
    def saySecondMessage(self):
        txt = ""
        return txt

    def exit_app():
        print("Infelizmente precisaremos encerrar.")    
        exit()