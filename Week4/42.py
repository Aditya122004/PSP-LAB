pwd=input("Enter your password: ")
lowercase=0
uppercase=0
digits=0
special=0
for i in pwd:
    if i>='a' and i<='z':
        lowercase=1
    elif i>='A' and i<='Z':
        uppercase=1
    elif i>='0' and i<='9':
        digits=1
    else:
        special=1
score=0
score=lowercase+uppercase+digits+special
if(score>=4 and len(pwd)>=8):
    print("Strong Password")
elif (score>=3 and len(pwd)>=8):
    print("Medium Password")
else:
    print("Weak Password")