row=int(input("Enter the number of rows:"))
i=0
j=0
for i in range(row+1,0,-1):
    for j in range(i):
        
        print("*",end='')
        j+=1
    print()
i+=1
j=1