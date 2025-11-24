import re
s=input("Enter string: ")
r=re.findall(r"\d[a-z]{2}\s\d{4}",s)
for i in r:
    print(i)
