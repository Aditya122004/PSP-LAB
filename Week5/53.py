import re
s=input("Enter string: ")
r=re.findall(r"\d+\.\d+(?:GHZ|GHz|ghz)",s)
for i in r:
    print(i)
