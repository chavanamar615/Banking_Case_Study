from abc import ABC,abstractmethod
class Account(ABC):
    def __init__(self,accno,name,balance):
        self.accno=accno
        self.name=name
        self.balance=balance
    
    @abstractmethod
    def deposite(self):
        pass
    
    def checkBalance(self):
        print(self.balance)
    
    @abstractmethod
    def calculateInterest(self):
        pass