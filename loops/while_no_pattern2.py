i=1
j=1
row=int(input("enter the number of rows "))
while i<=row:
    j=row
    while j>=i:

        print(j+1,end="")
        j-=1
    print()
    i+=1
    j=1
    
   