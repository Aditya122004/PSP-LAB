s=input("Enter string: ")
n=1
while(1):
    ch=input("Enter a character: ")
    if(len(ch)>1):
        print("Please enter only one character")
    else:
        idx=s.find(ch)
        if(idx!=-1):
            print(s[idx:idx+2])
        else:
            print(n)
            n=n+1
    choice=input("Enter yes to continue: ")
    if(choice != "yes"):
        break