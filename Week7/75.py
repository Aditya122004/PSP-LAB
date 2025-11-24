sen=input("Enter a sentence: ")
words=sen.split(" ")
l=[words[i] for i in range(1,len(words),2)]
print(l)