rollNo=input("Enter your Roll No")
if(len(rollNo)!=9):
    print("Invalid Roll No")
else:
    a=rollNo[:1]
    b=rollNo[1:3]
    c=rollNo[3:4]
    d=rollNo[4:6]
    e=rollNo[6:]
    if(a=="1"):
        print("You are a UG student")
    elif(a=="2"):
        print("You are a PG student")
    print("Your department code is",b)
    print("Your course code is",c)
    print(f"Your year of admission is 20{d}")
    print("Your class Roll no is",e)
    
