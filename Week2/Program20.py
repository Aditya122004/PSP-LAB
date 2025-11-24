n=int(input("Enter the number of lines: "))
for i in range(n):
    for space in range(i):
        print(end=" ")
    for star in range(n,i,-1):
        print("*",end=" ")
    print()
for i in range(1,n):
    for space in range(n,i+1,-1):
        print(end=" ")
    for star in range(i+1):
        print("*",end=" ")
    print()
