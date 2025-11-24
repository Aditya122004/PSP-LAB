import re
s=input("Enter string: ")
r=re.findall(r"\d{6}",s)
for i in r:
    print(i)
