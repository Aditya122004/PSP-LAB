import math 
def ncr(n,r):
    num=math.factorial(n)
    den=math.factorial(r)*math.factorial(n-r)
    return num//den
print(ncr(10,2))