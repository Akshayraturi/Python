a=float(input("Enter the first number a"))
b=float(input("Enter the second number b"))
c=float(input("Enter the third number c"))

if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif a==b and b==c and c==a:
    print("all are equal")
elif a==b or c==a:
    print("a and b are equal and  both are greater")
elif b==c or c==b:
    print("b and c are equal and both are greater")
else:
    print("c is greater ")