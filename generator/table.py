def generator(n):
    a=0
    b=int(input("enter the table number"))
    while a<n:
        a+=1
        yield a*b
for i in generator(10):
    print(i)

