date=int(input("Enter the date: "))
month=int(input("Enter the month: "))
year=int(input("Enter the year: "))
if(date>31 or month>12 or date<0 or month<0 or year<0):
    print("Invalid Date")
elif(date == 31 and (month != 1 or month !=3 or month !=5 or month !=5 or month !=7 or month !=8 or month !=10 or month !=12)):
     print("Invalid Date")
elif(date>=30 and month ==2):
    print("Invalid Date")
elif(date==29 and month==2 and (year%400!=0 and (year%4==0 and year%100==0))):
    print("Invalid Date")
else:
    print("Valid Date")
