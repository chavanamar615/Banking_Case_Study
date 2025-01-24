from account import Account
class Loan(Account):
    rate=0.03
    def __init__(self, accno, name,balance,repay=0,loanamt=100000):
        super().__init__(accno, name)
        self.balance=balance
        self.repay=repay
        self.loanamt=loanamt
        
    def calculateInterest(self):
        self.balance=self.balance*Loan.rate
    
    def Deposite(self):
        amount = int(input("Enter Amount"))
        if(amount<=self.loanamt):
            self.repay -= amount
            print(f"{amount} deposited Successfully please repay {self.repay}")
        else:
            self.balance+=amount
            print(f"{amount} Deposited Successfully!!!")
        