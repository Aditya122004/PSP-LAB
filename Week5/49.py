import re
s=input("Enter string: ")
r=re.findall(r"[A-Z]{2}[0-9]{6}",s)
for i in r:
    print(i)
