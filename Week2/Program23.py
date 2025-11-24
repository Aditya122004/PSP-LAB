currDay=int(input("Enter the current Date: "))
currMonth=int(input("Enter the current Month: "))
currYear=int(input("Enter the current year: "))
bDay=int(input("Enter your day of birth: "))
bMonth=int(input("Enter your month of birth: "))
bYear=int(input("Enter your year of birth: "))

days=currDay-bDay
if(days<=0):
    days+=30
    currMonth=currMonth-1
months=currMonth-bMonth
if(months<=0):
    months+=12
    currYear=currYear-1
years=currYear-bYear
if(years<0):
    print("Invalid Details Entered")
else:
    print("The difference between the dates is ",years," years",months," months and ",days," days ")
