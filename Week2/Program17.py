p=int(input("Enter the principal Amount: "))
n=int(input("Enter the time period in months: "))
r1=float(input("Enter the first rate of interest: "))
r2=float(input("Enter the second rate of interest: "))
r3=float(input("Enter the third rate of interest: "))
temp_r1=r1
temp_r2=r2
temp_r3=r3
r1=r1/1200
r2=r2/1200
r3=r3/1200
emi1=(p*r1*(1+r1)**n)/((1+r1)**n - 1)
emi2=(p*r2*(1+r2)**n)/((1+r2)**n - 1)
emi3=(p*r3*(1+r3)**n)/((1+r3)**n - 1)
print(f"The emi with {temp_r1}% interest rate is {emi1}")
print(f"The emi with {temp_r2}% interest rate is {emi2}")
print(f"The emi with {temp_r3}% interest rate is {emi3}")
