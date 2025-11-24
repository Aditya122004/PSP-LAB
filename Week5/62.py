import re
s=input("Enter string: ")
r=re.findall(r"[A-Z]{3}[A-Z]{2}[0-9]{4}\w",s)
for i in r:
    print(i)
