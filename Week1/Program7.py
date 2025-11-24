import math
radius1=float(input("Enter the radius of first Pizza: "))
radius2=float(input("Enter the radius of second Pizza: "))
price1=int(input("Enter the price of first Pizza: "))
price2=int(input("Enter the price of second Pizza: "))
if(radius1<=0 or radius2<=0 or price1<=0 or price2<=0):
    print("Invalid Data Entered")
else:
    area1=math.pi*radius1*radius1
    area2=math.pi*radius2*radius2
    val1=area1/price1
    val2=area2/price2
    if(val1>val2):
        print("Pizza 1 has better value")
    else:
        print("Pizza 2 has better value")

