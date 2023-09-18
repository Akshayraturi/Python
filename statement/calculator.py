op=str(input("enter the operator"))
a=float(input("enter the first number"))
b=float(input("enter the second number"))
import math
if op=="+":
  print(a,"+",b,"=",a+b)
elif op=="-":
  print(a,"-",b,"=",a-b)
elif op=="*":
  print(a,"*",b,"=",a*b)
elif op=="/":
  print(a,"/",b,"=",a/b)
elif op=="**":
  print(a,"**",b,"=",a**b)
elif op=="//":
  print(a,"//",b,"=",a//b)
elif op=="~":
  print("square root of",a,"is:",math.sqrt(a),"AND","square root of",b,"is:",math.sqrt(b))

