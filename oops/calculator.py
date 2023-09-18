class Calculator:
    def __init__(self,operator):
        self.operator=operator
    def add(self):
        if self.operator=="+":
            print("I can add almost 5 number")
            a=float(input("enter the 1st number"))
            b=float(input("enter the 2nd number"))
            c=float(input("enter the 3rd number"))
            d=float(input("enter the 4th number"))
            e=float(input("enter the 5th number"))
            print("The sum of these numbers are",a+b+c+d+e)
    def subtract(self):
        if self.operator=="+":
            a=float(input("enter the 1st number"))
            b=float(input("enter the 2nd number"))
            print("The subtraction of these numbers are",a-b)




            
            



