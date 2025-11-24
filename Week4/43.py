s1=input("Enter the first string: ")
s2=input("Enter the second string: ")
s=""
i=0
j=0
while(i<len(s1) and j<len(s2)):
    s=s+s1[i]
    s=s+s2[j]
    i=i+1
    j=j+1
while(i<len(s1)):
    s=s+s1[i]
    i=i+1
while(j<len(s2)):
    s=s+s2[j]
    j=j+1
print(s)