import re
s=input("Enter string: ")
r=re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",s)
for i in r:
    print(i)
