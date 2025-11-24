def dectobin(n):
    if n==0:
        return ""
    return dectobin(n//2)+str(n%2)
print(dectobin(10))