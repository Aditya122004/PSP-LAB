str1=input("Enter first string: ")
str2=input("Enter second string: ")
str1=str1.lower()
str2=str2.lower()
str1=str1.strip()
str2=str2.strip()
ans=""
for i in range(len(str1)):
    for j in range(i+1,len(str1)+1):
        temp=str1[i:j]
        if(str2.find(temp)!=-1):
            if(len(temp)>len(ans)):
                ans=temp
if(len(ans)==0):
    print("No Common Substring")
else:
    print("The longest common Substring is",ans) 
