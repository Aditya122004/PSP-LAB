import re
s=input("Enter string: ")
r=re.findall(r"#[0-9A-F]{6}",s)
for i in r:
    print(i)
