n=int(input("Enter the number: "))
temp=n1=n
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
    print("Armstrong Number")
else:
    print("Not an Armstrong number")
