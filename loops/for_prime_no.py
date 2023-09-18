n=int(input("Enter the number"))
if n==0 or n==1:
    print("neither prime nor composite ")
elif n>1:
    for i in range(2,n):
        if(n%i == 0):
             print("Prime number")
             break
    else:
        print("Composite number")