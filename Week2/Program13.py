healthStatus=int(input("Enter health status: "))
age=int(input("Enter the age: "))
gender=input("Enter male or female: ")
place=input("Enter city or village: ")
insured=0
maxAmount=0
maxPremium=0
if(healthStatus==1 and (age>=25 and age<=35) and place=="city"):
    insured=1
    if(gender=="male"):
        maxPremium=8000
        maxAmount=200000
    elif(gender=="female"):
        maxPremium=15000
        maxAmount=300000
elif(healthStatus==2 and (age>=25 and age<=35) and place=="village" and gender=="male"):
    insured=1
    maxAmount=100000
    maxPremium=6000
if(insured):
    print("The person can be insured")
    print("The maximum Amount insured can be ",maxAmount)
    print("The maximum premium can be ",maxPremium)
else:
    print("The person cannot be insured")
