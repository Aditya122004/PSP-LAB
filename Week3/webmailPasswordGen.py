bGrp=input("Enter your blood Group")
bday=int(input("Enter your date of birth"))
bMonth=input("Enter your month of birth")
phoneNo=input("Enter last three digits of your mobile Number")
pwd=""
bGrp=bGrp.upper()
bGrp=bGrp[:1]
bMonth=bMonth.lower()
bMonth=bMonth[:3]
if(bday<10):
    temp=bday
    bday="0"+str(temp)
else:
    bday=str(bday)
pwd+=bGrp
pwd+=bMonth
pwd+=bday
pwd+=phoneNo
print("Your webmail password is",pwd)
