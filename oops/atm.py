class atm:
    def __init__(self,cash,pincode,name,phone):
        self.name=name
        self.phone=phone
        self.cash=cash
        self.pincode=pincode
    def deposit(self,pin,amount):
        if pin==self.pincode:
            print("Previous bank balance:",self.cash)
            print("Deposited amount",amount)
            self.cash=self.cash+amount
            print("The amount now in your account is",self.cash)
            print("The amount left in your account is",self.cash)
        else:
                print("You are entering wrong pincode")
    def withdraw(self,pin,amnt):
        if pin==self.pincode:
            print("Previous bank balance:",self.cash)
            self.cash=self.cash-amnt
            print("Deposited amount",amnt)
            print("The amount left in your account is",self.cash)
        else:
            print("You are entering wrong pincode")
    def cashbook(self,pin):
        
    def printme(self,code):
        if code==self.pincode:
            print("Name:",self.name)
            print("Mobile number",self.phone)
            print("Total cash:",self.cash)
            print("Pincode",self.pincode)
        else:
            print("You are entering wrong pincode")
            
            
akshay=atm(50000,7683,"Akshay",9389982899)
#akshay.deposit((int(input("Enter the pin:"))),int(input("Enter the amount you want to deposit")))
akshay.printme((int(input("Enter the pin:"))))