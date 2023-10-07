class Bankaccount:
    def __init__(self,acnum,balance,dateofopening,customer_name):
        self.customer_name=customer_name
        self.account_number=acnum
        self.balance=balance
        self.date_of_opening=dateofopening
    def deposit(self,amount):
        print("Previous Bank balance:",self.balance)
        print("Deposited amount:",amount)
        self.balance=self.balance+amount
        print("New bank balance:",self.balance)
    def withdraw(self,amount):
        print("Previous Bank balance:",self.balance)
        print("Withdraw amount:",amount)
        if amount>self.balance:
            print("Amount is more than bank balance")
        else:
            self.balance=self.balance-amount
            print("New bank balance:",self.balance)
    def check_balance(self):
        print("Your current bank balance is:",self.balance)
    def printme(self):
        print("Customer name:",self.customer_name)
        print("Account number:",self.account_number)
        print("Bank balance:",self.balance)
        print("Date of opening",self.date_of_opening)

obj=Bankaccount(20848028849,25000,"21-03-2023","Akshay")
obj2=Bankaccount(48594784949,2500,"21-03-2022","Manvar")
obj3=Bankaccount(940848409749,15000,"2-09-1998","Naitik")
print("-----Previous details--------")
obj.printme()
print("------------------")
obj2.printme()
print("------------------")
obj3.printme()
print("------------------")
print("------Updated details-----")
obj.printme()
obj.deposit(25000)
print("------------------")
obj2.printme()
obj2.withdraw(1000)
print("------------------")
obj3.printme()
obj3.withdraw(10000)
print("------------------")