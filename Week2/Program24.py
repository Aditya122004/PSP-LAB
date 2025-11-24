n=int(input("Enter a number"))
f=False
for i in range(2,n):
    if n%i==0:
        f=True
        break
if(f):
    print("Not a prime number")
else:
    print("Prime number")
        