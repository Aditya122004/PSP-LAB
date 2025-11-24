name=input("Enter the full Name: ")
w=name.split(" ")
n=""
for i in range(0,len(w)-1):
    n=n+w[i][0]+"."
n=n+w[len(w)-1]
print(n)