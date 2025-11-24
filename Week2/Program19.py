n1=int(input("Enter the first number of the range: "))
n2=int(input("Enter the ending number of the range: "))
for i in range(n1,n2+1):
    temp=n1=n=i
    c=0
    s=0
    while(n1!=0):
        c=c+1
        n1=n1//10
    while(n!=0):
        d=n%10
        s=s+d**c
        n=n//10
    if(s==temp):
        print(i)
