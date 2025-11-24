p=input("Enter sentence: ")
w=input("Enter the word to be searched: ")
words=p.split(" ")
cnt=0
for i in words:
    if(i == w):
        cnt=cnt+1
print(f"The frequency of {w} is {cnt}")