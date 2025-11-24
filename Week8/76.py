def isArmstrong(num):
    s=str(num)
    p=(len(s))
    temp=num
    sum=0
    while(temp!=0):
        d=temp%10
        sum+=d**p
        temp=temp//10
    if sum==num:
        return True
    else:
        return False
print(isArmstrong(153))
print(isArmstrong(10))