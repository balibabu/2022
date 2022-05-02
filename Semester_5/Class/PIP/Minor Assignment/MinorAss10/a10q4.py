'''
4. Write a python class BankAccounts to model a bank accounts maintenance system:
a. To create bank account (name, account number),
b. To deposit money and withdraw money
c. To check minimum acc balance before withdraw and display message when withdraw amount violates the minimum acc balance condition,
d. Give options to open, deposit, withdraw and display acc balance.
'''

class BankAccounts:
    def __init__(self,name,ac_no):
        self.name = name
        self.ac_no=ac_no
        print('a/c created successfully . . .')
        print('deposit some money')
        self.balance=int(input('enter amount:'))

    def deposit(self,money):
        self.balance+=money
        print('your account is credited with amount Rs',money)

    def withdraw(self,money):
        if(self.balance-money>100):
            self.balance-=money
            print('you balance is deducted by Rs',money)
        else:
            print('sorry!! withdraw amount violates the minimum acc balance condition')
    def display(self):
        # print('Name:',self.name)
        # print('A/c number:',self.ac_no)
        print('Current Balance:',self.balance)

def personal(account):
    print('\nMenu:\n1.Exit\n2.Deposit\n3.Withdraw\n4.Display a/c balance')
    while True:
        choice = int(input('enter your choice:'))
        if choice == 1:
            break
        elif choice == 2:
            account.deposit(int(input('enter amount:')))
        elif choice == 3:
            account.withdraw(int(input('enter amount:')))
        elif choice == 4:
            account.display()
        else:
            print('invalid choice')
    print('\n\n' )

def main():
    accounts = {}
    while True:
        print('\nMenu:\n0.Exit\n1.Open Bank Account\n2.Already Have\n3.List all accounts')
        choice1=int(input('enter your choice:'))
        if choice1==0:
            break

        elif choice1==1:
            name = input('enter your name:')
            ac_no = int(input('enter account number:'))
            if not ac_no in accounts:
                accounts[ac_no] = BankAccounts(name, ac_no)
            else:
                print('sorry!! account number already present')
        elif choice1==2:
            ac_no=int(input('enter your account number:'))
            try:
                personal(accounts[ac_no])
            except:
                print('sorry! No account found')
        elif choice1 == 3:
            print('printing the list of accounts:')
            for i in accounts:
                print(i)
        else:
            print('invalid choice')


if __name__ == '__main__':
    main()