bin=int(input("Enter the number in binary: "))
exp=1
dec=0
while(bin>0):
    d=bin%10
    dec=dec+(exp*d)
    exp=exp*2
    bin=bin//10
print("The decimal number is ",dec)
octal=""
while(dec!=0):
    d=dec%8
    octal+=str(d)
    dec=dec//8
octal=octal[::-1]
print("The octal value is ",octal)
