def generator(n):
    yield n*n*n
for i in generator((float(input("enter the number")))):
    print(i)

