from account import Account
from current import Current
from savingaacc import Saving
from salary import Salary
from loan import Loan
class Bank():
    def __init__(self,accno,name,balance):
        self.accno=accno
        self.name=name
        self.balance=balance
        self.list_acc=[]
    def createAccount(self):
        ch=0
        while(ch!=5):
            print("1.Saving \n2.current \n3.Loan \n4.salary \n5.Exit")
            ch=int(input("enter your choice:"))
            
            if(ch==1):
                accno=int(input("enter accno:"))
                name=input("Name of accholder:")
                s=Saving(accno, name,balance=0,min=10000)
                self.list_acc.append(s)
                
            elif(ch==2):
                accno=int(input("enter accno:"))
                name=input("Name of accholder:")
                c=Current(accno, name,balance=0,od=0,olimit=50000)
                self.list_acc.append(c)
                
            elif(ch==3):
                accno=int(input("enter accno:"))
                name=input("Name of accholder:")
                l=Loan(accno, name,balance=0,repay=0,loanamt=100000)
                self.list_acc.append(l)
                
            elif(ch==4):
                accno=int(input("enter accno:"))
                name=input("Name of accholder:")
                sal=Salary(accno,name)
                self.list_acc.append(sal)
                
            elif(ch==5):
                print("exit")
            else:
                print("your choice is not matching")   
                     
    def counter(self):
        print("1.Deposite \n2.Withdraw \n3.checkBalance")
        ch=0
        if(ch==1):
            accno=int(input("enter your account number:"))
            for x in self.list_acc:
                if(x.accno==accno):
                    x.deposite()
                
        elif(ch==2):
            accno=int(input("enter your account number:"))
            for x in self.list_acc:
                if(x.accno==accno):
                    x.withdraw()
                    
        elif(ch==3):
            accno=int(input("enter your account number:"))
            for x in self.list_acc:
                if(x.accno==accno):
                    x.checkBalance()
        elif(ch==4):
            accno= int(input("Enter your account number: "))
            for i in self.list_acc:
                if accno in self.list_of_accounts:
                    i.calculateInterest()
        else:
            print("choice is invalid")
            
    def deleteAccount(self):
        accno=int(input("enter your account number:"))
        for i in self.list_acc:
                if(accno in self.list_acc):
                    self.list_acc.remove(i)
                    
                    
                    



                
                    
                    
                    
                    
                    