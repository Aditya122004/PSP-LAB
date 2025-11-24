import re
s=input("Enter string: ")
r=re.findall(r"i\d{1,2}\s\d{1,2}(?:gen|Gen|GEN)",s)
for i in r:
    print(i)
