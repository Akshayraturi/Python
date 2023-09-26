def add(hin,math,eng,sst,sci,IT,):
    return hin+math+eng+sst+sci+IT
def per(obt):
    return obt/600*100
def avg(num):
    return num/7
def grade(percent):
    if percent==100 or percent>90:
        return "A+ "
    elif percent<=90 or percent>80:
        return "B"
    elif percent<=80 or percent>70:
        return "C"
    elif percent<=70 or percent>60:
        return "D"
    elif percent<=60 or percent>50:
        return "E"
    else:
        return "F"
x=add(float(input("enter the numbers in hindi:")),float(input("enter the numbers in math:")),
float(input("enter the numbers in english:")),float(input("enter the numbers in social science:")),
float(input("enter the numbers in science:")),float(input("enter the numbers in computer:")))
if x>600:
    print("\nPlease enter the number lower than 100")
else:
    print("\nTotal marks are:",x,"/600")
    print("Percentage:",per(x))
    print("Average marks:",avg(x))
    print("Grade",grade(per(x)))


