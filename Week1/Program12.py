units=float(input("Enter the number of units consumed: "))
if(units<0):
    print("Invalid Values Entered")
else:
    if(units<200):
        cost=0.5*units
    elif(units<=400):
        cost=100+0.65*(units-200)
    elif(units<=600):
        cost=100+130+0.80*(units-400)
    else:
        cost=100+130+160+(units-600)*1.25
    print("The bill is ",cost)
 
