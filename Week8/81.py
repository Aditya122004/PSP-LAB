def add_sub(A,B,operation='add'):
    rows_A=len(A)
    cols_A=len(A[0])
    c=[]
    for i in range(rows_A):
        row=[]
        for j in range(cols_A):
            if operation=='add':
                row.append(A[i][j]+B[i][j])
            else:
                row.append(A[i][j]-B[i][j])
        c.append(row)
    return c
def multiply(A,B):
    rows_A=len(A)
    cols_A=len(A[0])
    cols_B=len(B[0])
    c=[[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                c[i][j]+=A[i][k]*B[k][j]
    return c
A=[[1,2,3],[2,3,4],[3,4,5]]
B=[[1,2,3],[2,3,4],[3,4,5]]
print(add_sub(A,B))
print(multiply(A,B))
