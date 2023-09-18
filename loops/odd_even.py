i=int(input("Enter the start"))
range=int(input("Enter the range "))

if range>0:
    while i<=range:
        if i%2==0:
            print(i,"even number")
        else:
            print(i,"odd number")
        i+=1
elif range<=0:
    while i>=range:
        if i%2==0:
            print(i,"even number")
        else:
            print(i,"odd number")
        i-=1
       