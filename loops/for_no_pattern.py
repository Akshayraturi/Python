

row=int(input("Enter the number of rows:"))
i=1
j=1
for i in range(row):
    for j in range(i+1):
        j+=1
        print(j,end='')
        
    print()
i+=1
j=1