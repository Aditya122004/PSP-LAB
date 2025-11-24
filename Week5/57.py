import re
s=input("Enter string: ")
r=re.findall(r"CA\d{3}",s)
for i in r:
    print(i)
