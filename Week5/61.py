import re
s=input("Enter string: ")
r=re.findall(r"[A-Z]{4}0\w{6}",s)
for i in r:
    print(i)
