p=float(input("Enter the principal Amount: "))
r=float(input("Enter the rate of interest: "))
n=float(input("Enter the time period in months: "))
if(p<=0 or r<=0 or n<=0):
    print("Invalid Data Entered")
else:
    r=r/1200
    EMI=(p*r*(1+r)**n)/((1+r)**n - 1)
    print("The EMI is ",EMI)
