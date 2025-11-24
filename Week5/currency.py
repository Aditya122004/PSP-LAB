import re
s=input("Enter string: ")
r=re.findall(r"(?:\$|RS|Rs|rs)\d+\.?\d*",s)
for i in r:
    print(i)
