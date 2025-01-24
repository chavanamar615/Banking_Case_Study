from savingaacc import Saving
from datetime import datetime,timedelta
class Salary(Saving):
    def _init_(self, accno, name, balance = 0 , min_bal = 0, rate=4,last_transaction_date=datetime.now(),inactivity_time= timedelta(days=60)):
        super()._init_(accno, name, balance, min_bal, rate)
        self.last_trasaction_date = last_transaction_date
        self.inactivity_time = inactivity_time
        self.inactivity = timedelta(days=60)
        
    def withdraw(self, amount):
        super().withdraw(amount)
        self.last_trasaction_date = datetime.now()

    def deposite(self, amount):
        super().deposite(amount)
        self.last_trasaction_date = datetime.now()


    def checkActivty(self):
        current_date = datetime.now()
        if(current_date - self.last_trasaction_date) > self.inactivity_time:
            print("account is frozen")
        else:
            print("account is active")

s2 = Salary(7,"amar",balance=40000,inactivity_time=timedelta(days=60))

