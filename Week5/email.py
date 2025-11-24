import re
s=input("Enter string: ")
r=re.findall(r"[\w\.]+@\w+\.\w+",s)
for i in r:
    print(i)
