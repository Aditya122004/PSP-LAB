import re
s=input("Enter string: ")
r=re.findall(r"[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}",s)
for i in r:
    print(i)
