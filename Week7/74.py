sen=input("Enter a sentence: ")
words=sen.split(" ")
l=[word[::-1] if i%2==0 else word for  i,word in enumerate(words)]
print(l)