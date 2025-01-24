from account import Account
class Current(Account):
    def __init__(self, accno, name,balance,od=0,olimit=50000):
        super().__init__(accno, name)
        self.balance=balance
        self.od=od
        self.overlimit=olimit
    def checkLimit(self):
        print("limit of account is")
    
    def withdraw(self):
        amount=int(input("enter amount:"))
        if(amount<self.balance):
            self.balance=self.balance-amount
        elif(amount>self.balance and amount<self.overlimit):
            self.od=amount-self.balance
        elif(amount>self.balance and amount>self.overlimit):
            print("Not allowed")
            
    def deposite(self):
        amount=int(input("enter your amount to deposite:"))
        if(self.balance>amount and self.balance>self.od):
            self.balance=self.balance+amount
        elif(self.balance<amount and self.od>self.balance):
            self.balance=amount-self.od
    