age=int(input("Enter your age"))
if age>=0 and age<=12:
    print("You are kid")
elif age>=13 and age<=19:
    print("You are teenager")
elif age>=20 and age<=60:
    print("You are Adult")
else:
    print("you are a Senior citizen")