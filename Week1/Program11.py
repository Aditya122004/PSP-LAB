x=int(input("Enter the value of x: "))
n=int(input("Enter the value of n: "))
if(n==0):
    y=x
elif(n==1):
    y=x+1
elif(n==2):
    y=x**2+n
else:
    y=x**n

print("The value of y is ",y)
