str1=input("Enter first string: ")
str2=input("Enter second string: ")
str1=str1.lower()
str2=str2.lower()
str1=str1.strip()
str2=str2.strip()
arr=[0]*26
for i in str1:
    c=ord(i)-97
    arr[c]=arr[c]+1
for i in str2:
    c=ord(i)-97
    arr[c]=arr[c]-1
f=True
for i in range(26):
    if(arr[i]!=0):
        f=False
        break
if(f):
    print("Anagram")
else:
    print("Not an Anagram")
