from account import Account
class Saving(Account):
    rate=0.03
    def __init__(self, accno, name,balance=0,min=10000):
        super().__init__(accno, name,balance)
        self.minimum = min
    
    def calculateInterest(self):
       self.balance=self.balance+self.balance*Saving.rate
    
    def withdraw(self):
        amount=int(input("enter amount you have to withdraw:"))
        if(self.balance-amount>=self.minimum):
            self.balance=self.balance-amount
        else:
            print("Your balance is below 10000")
    
    def deposite(self):
        amoount=int(input("enter amount which you have to deposite:"))
        self.balance=self.balance+amoount            
            
       
    
    
     
    
    
    
        
        
  
        