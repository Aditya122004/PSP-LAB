import re
s=input("Enter string: ")
r=re.findall(r"[IVXLCDM]+",s)
for i in r:
    print(i)
