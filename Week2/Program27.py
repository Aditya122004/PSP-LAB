n1=int(input("enter first number in range"))
n2=int(input("Enter second number in range"))
for i in range(n1,n2+1):
    num=i
    f=False
    for j in range(2,num):
        if num%j==0:
            f=True
            break
    if(not f):
        print(num,end=" ")