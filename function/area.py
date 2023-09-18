def rect(l,b):
    return l*b
def circle(r):
    return r*r
def sqr(side):
    return side*side
def tri(b,h):
    return 1/2*b*h
print(rect(int(input("enter the length")),int(input("enter the breadth"))))
print()
print(circle(int(input("enter the radius"))))
print()
print(sqr(int(input("Enter the side of the square"))))
print()
print(tri(int(input("enter the base")),int(input("enter the height"))))
