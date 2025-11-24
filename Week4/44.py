s=input("Enter the sentence: ")
mask=input("Enter the mask: ")
words=s.split(" ")
st=""
for i in range(len(words)):
    if(len(words[i])%2!=0):
        st=st+words[i]+str(i)
        words[i]=mask
s=""
for i in words:
    s=s+i+" "
print(s)
print(st)