x=float(input("Enter the x-cordinate"))
y=float(input("Enter the y-cordinate"))
if(x==0 and y==0):
    print("Origin")
elif(x==0):
    print("Y-axis")
elif(y==0):
    print("X-axis")
elif(x>0 and y>0):
    print("1st Quadrant")
elif(x<0 and y>0):
    print("2nd Quadrant")
elif(x<0 and y<0):
    print("3rd Quadrant")
else:
    print("4th Quadrant")
