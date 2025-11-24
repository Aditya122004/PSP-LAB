decimal=int(input("Enter the number in decimal: "))
tem=decimal
bin=""
while(decimal!=0):
    d=decimal%2
    bin+=str(d)
    decimal=decimal//2
bin=bin[::-1]
print("The binary value is ",bin)
decimal=tem
octal=""
while(decimal!=0):
    d=decimal%8
    octal+=str(d)
    decimal=decimal//8
octal=octal[::-1]
print("The octal value is ",octal)
