'''Define a class Account, having attributes account holder’s name, account number, account type, the
amount deposited and minimum deposit amount. Define two classes, namely Savings and Current.
The Savings class should have a property interest. Define __init__ method for all these classes. Also,
define get and set methods to determine and set the value of the data attributes.
'''
class Account:

    def __init__(self,name,account_no,typ,amt_deposited,min_deposit_amt):
        self.min_deposit_amt = min_deposit_amt
        self.typ = typ
        self.name = name
        self.account_no=account_no
        self.amt_deposited=amt_deposited

    def set(self):
        setattr(self, input("What you want to change? \nname,account_no,type,amt_deposited\n"), input("Enter the value:"))

    def get(self):
        return getattr(self,input('what do you want? '))

    def __str__(self):
        return f'Name:{self.name.title()}\nA/c number:{self.account_no}\nType:{self.typ}\nAmount deposited:{self.amt_deposited}\nMinimum deposite:{self.min_deposit_amt}\n'                          # new printing style

class Savings(Account):
    def __init__(self,name,account_no,amt_deposited,min_deposit_amt):
        super().__init__(name,account_no,'Saving Account',amt_deposited,min_deposit_amt)

    def intreset(self,time,rate):
        total=self.min_deposit_amt+self.amt_deposited
        return (total*rate*time)/100


class Current(Account):
    def __init__(self, name, account_no, amt_deposited, min_deposit_amt):
        super().__init__(name, account_no, 'Current Account', amt_deposited,min_deposit_amt)


s=Savings('bali babu',123,500,100)
print(s)
s.set()
print(s.get())


