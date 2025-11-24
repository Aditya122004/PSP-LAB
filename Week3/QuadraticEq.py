import math
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=b**2-4*a*c
if(d<0):
    print("There exists no real roots")
elif(d==0):
    print("The roots are equal")
    x1=(-b)/2*a
    print("The value of the root is ",x1)
else:
    print("The roots are distinct")
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b-math.sqrt(d))/2*a
    print("The first root is ",x1)
    print("The second root is ",x2)
