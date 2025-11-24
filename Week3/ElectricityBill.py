accNo=int(input("Enter Account Number:"))
code=input("Enter code:")
code=code.upper()
codes=["R","I","C"]
if(len(code)>1 or code not in codes):
    print("Invalid Code")
else:
    cost=0
    if(code=="R"):
        kwh=float(input("Enter the usage:"))
        cost= 6+0.052*kwh
    elif(code=="I"):
        pkwh=float(input("Enter usage during peak hours: "))
        opkwh=float(input("Enter usage during off peak hours: "))
        if(pkwh>0):
            pcost=76
            pkwh=pkwh-1000
            if(pkwh>0):
                pcost+=0.065*pkwh
            cost+=pcost
        if(opkwh>0):
            opcost=40
            opkwh=opkwh-1000
            if(opkwh>0):
                opcost+=0.028*opkwh
            cost+=opcost
    elif(code=="C"):
        kwh=float(input("Enter the usage:"))
        cost=60
        kwh=kwh-1000
        if(kwh>0):
            cost+=0.045*kwh
    print(f"The amount due is ${cost}")
