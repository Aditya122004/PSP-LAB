import re
s=input("Enter string: ")
r=re.findall(r"(?:AB|[ABO])[+-]",s)
for i in r:
    print(i)
