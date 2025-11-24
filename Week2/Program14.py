print("The first 5 numbers of hexagonal series are:")
for i in range(1,6):
    curr=2*(i**2)-i
    print(curr,end=" ")
n=6
print()
ch=input("Enter yes to print the next term of the series: ")
while(ch=="yes"):
    curr=2*(n**2)-n
    print(curr)
    n=n+1
    ch=input("Enter yes to print the next term of the series: ")
    
