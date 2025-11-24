import re
s=input("Enter string: ")
r=re.findall(r"(?:0[1-9]|1[0-2]):(?:[0-5]\d):(?:[0-5]\d)\s?(?:AM|PM)",s)
for i in r:
    print(i)
