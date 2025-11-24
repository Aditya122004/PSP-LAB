import re
s=input("Enter string: ")
r=re.findall(r"https:[/]{2}www\.\w+\.\w+",s)
for i in r:
    print(i)
