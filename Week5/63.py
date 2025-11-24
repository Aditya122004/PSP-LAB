import re
s=input("Enter string: ")
r=re.findall(r"[0-9]{2}\w{10}\dZ\d",s)
for i in r:
    print(i)
