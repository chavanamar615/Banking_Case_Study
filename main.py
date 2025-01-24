from account import Account
from current import Current
from savingaacc import Saving
from salary import Salary
from loan import Loan
from bank import Bank
b=Bank()

while(True):
            print("1.Create account \n2.counter activities \n3.close \n4.Display bank credintial \n5.Exit")
            ch=int(input("enter your choice:"))  
            
            if(ch==1):
                b.createAccount()
            elif(ch==2):
                b.counter()
            elif(ch==3):
                b.deleteAccount()
                break  
            else:
                print("enter valid choice")
                
                
                  
    