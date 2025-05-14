import datetime
hour = datetime.datetime.now().hour
class Waiter:
    def __init___(self, db):

        self.date = date.today().strftime("%d-%m-%Y")
        self.__greeting = "Bom dia!" if 5<=hour<12 else "Boa tarde!" if hour<18 else "Boa noite!"
        self.__interaction_n = 0
        self._txt = [" 1 - Listar Tópicos \n 2 - Listar Tópicos e Companias \n 0 - sair"]

        self.db = db
    
    def beginService(self):
        print(self.__greeting)
        self.listOptions()

    def listOptions(self):
        print("Para continuar, digite o número correspondente a opção desejada")
        choice = input(self.getText())

        self.__interaction += 1

    def getText(self):

        if self.__interaction_n == 0:
            print(self._txt[0])
            return
        
        print(self._txt[1])
        
    def greetings(self):
        text = " 1 - Listar Tópicos \n 2 - Listar Tópicos e Companias \n 0 - sair"