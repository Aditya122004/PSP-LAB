sen=input("Enter a sentence: ")
words=sen.split(" ")
l=[word[:len(word)//2][::-1] + word[len(word)//2:][::-1]
    for word in words]
print(l)