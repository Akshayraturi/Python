class calculator:
    def __init__(self):
        pass
    def add(self,a,b,c,d,e):
        print("The sum of these numbers are:",a+b+c+d+e)
    def subtract(self,a,b):
        print("The subtraction of these numbers are",a-b)
    def divide(self,a,b):
        print("The subtraction of these numbers are:",a/b)
    def multiply(self,a,b,c,d,e):
        print("The  of these numbers are:",a*b*c*d*e)
    def root(self,a):
        import math
        print("The root of the number is: ",math.sqrt(a))
    def square(self,a):
        print("The root of the number is: ",a*a)
    def cube(self,a):
        print("The root of the number is: ",a*a*a)
cal=calculator()
print("          ***************CALCULATOR****************          ")
op=(int(input("Choose what do you want to do:\n1.add\n2.subtract\n3.divide\n4.multiply\n5.Root\n6.square\n7.cube\n8.Exit\n"))) 
if op==1:
    print("I can add almost 5 number")
    cal.add(float(input("enter the 1st number:")),float(input("enter the 2nd number:")),float(input("enter the 3rd number:")),float(input("enter the 4th number:")),float(input("enter the 5th number:")))
elif op==2:
    cal.subtract(float(input("enter the 1st number:")),float(input("enter the 2nd number:")))
elif op==3:
    cal.divide(float(input("enter the 1st number:")),float(input("enter the 2nd number:")))
elif op==4:
    print("I can multiply almost 5 number:")
    cal.multiply(float(input("enter the 1st number:")),float(input("enter the 2nd number:")),float(input("enter the 3rd number:")),float(input("enter the 4th number:")),float(input("enter the 5th number:")))
elif op==5:
    cal.root(float(input("enter the number:")))
elif op==6:
    cal.square(float(input("enter the number:")))
elif op==7:
    cal.cube(float(input("enter the number:")))
else:
    print("exited......")



        

    
    




            
            



