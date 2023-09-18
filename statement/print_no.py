i=int(input("Enter the start"))
range=int(input("Enter the range "))

if range>0:
    while i<=range:
        print(i)
        i+=1
elif range<=0:
    while i>=range:
        print(i)
        i-=1