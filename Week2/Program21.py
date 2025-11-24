n=int(input('''Enter 1 for sin series
Enter 2 for cos series
Enter 3 for exponential series
Enter your choice: '''))
if(n==1):
    y=int(input("Enter the number of terms you want to print: "))
    sign=1
    print("sinx =",end=" ")
    for i in range(y):
        if(sign==1):
            if(i==y-1):
                print(f"x^{2*i+1}/{2*i+1}!",end="")
            else:
                print(f"x^{2*i+1}/{2*i+1}!",end="-")
        else:
            if(i==y-1):
                print(f"x^{2*i+1}/{2*i+1}!",end="")
            else:
                print(f"x^{2*i+1}/{2*i+1}!",end="+")
        sign=sign*-1
elif(n==2):
    y=int(input("Enter the number of terms you want to print: "))
    print("cosx =",end=" ")
    print("1-",end="")
    sign=-1
    for i in range(y-1):
        if(sign==1):
            if(i==y-2):
                print(f"x^{2*(i+1)}/{2*(i+1)}!",end="")
            else:
                print(f"x^{2*(i+1)}/{2*(i+1)}!",end="-")
        else:
            if(i==y-2):
                print(f"x^{2*(i+1)}/{2*(i+1)}!",end="")
            else:
                print(f"x^{2*(i+1)}/{2*(i+1)}!",end="+")
        sign=sign*-1
elif(n==3):
    y=int(input("Enter the number of terms you want to print: "))
    print("e^x =",end="")
    print("1",end="+")
    for i in range(1,y):
        if(i==y-1):
            print(f"x^{i}/{i}!",end="")
        else:
            print(f"x^{i}/{i}!",end="+")
else:
    print("Wrong Choice Entered")
