a=int(input("Enter the first number a"))
b=int(input("Enter the second number b"))
c=int(input("Enter the third number c"))
d=int(input("Enter the fourth number d "))
if a>b and a>c and a>d:
    print("a is greater")
elif b>a and b>c and d<b:
    print("b is greater")
elif c>a  and d<c:
    print("c is greater")
elif a==b  :
    print("a and b are equal and  both are greater")
elif a==c:
    print("a and c are equal and  both are greater")
elif a==d:
    print("a and d are equal and  both are greater")
elif c==d:
    print("b and c are equal and  both are greater")
else:
    print("d is greater ")