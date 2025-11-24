n=int(input("Enter the number of lines: "))
for i in range(n+1):
    for j in range(n-i+1):
        print(end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+2):
        print(end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    print()
