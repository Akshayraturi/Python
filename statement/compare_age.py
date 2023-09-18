a=str(input("enter the name of first student:"))
b=str(input("enter the name of second student:"))
c=str(input("enter the name of third student:"))
print()
x=int(input("Enter the age of first student: "))
y=int(input("Enter the age of second student:"))
z=int(input("Enter the age of third student: "))
print()
if x>y and x>z:
    print(a,'is older student')
if y>x and y>z:
    print(b,'is older student')
if z>x and z>y:
    print(c,'is older student')