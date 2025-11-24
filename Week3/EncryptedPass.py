pwd=input("Enter password to be encrypted: ")
encPass=""
for i in pwd:
    c=ord(i)
    if(i=='z'):
        encPass+='a'
    else:
        encPass+=chr(c+1)
print("The encrypted password is ",encPass)
pwd2=input("Enter the password to be decryped: ")
decPass=""
for i in pwd2:
    c=ord(i)
    if(i=='a'):
        decPass+='z'
    else:
        decPass+=chr(c-1)
print("The decrypted password is ",decPass)

