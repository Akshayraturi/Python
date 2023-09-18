l=[1,2,3,4,3,5,476,7,76]
odd=0
even=0
for i in l:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(l)
print("There are",even,"even numbers in this list")
print("There are",odd,"odd numbers in this list")