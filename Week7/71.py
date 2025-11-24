rows=int(input("Enter the number of rows: "))
pat1=[[j for j in range(1,i+1)] for i in range(1,rows+1)]
print(pat1)
pat2=[[j for j in range(rows,i-1,-1)] for i in range(1,rows+1)]
print(pat2)