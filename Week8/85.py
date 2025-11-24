def nCr(n,r):
    if r==0 or r==n:
        return 1
    return nCr(n-1,r-1)+nCr(n-1,r)
def pascal(rows):
    for n in range(rows):
        print(""*(rows-n),end="")
        for r in range(n+1):
            print(nCr(n,r),end=" ")
        print()
print(pascal(5))