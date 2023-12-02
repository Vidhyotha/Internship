text=input('enter a sentence')
text=text.lower()
words=text.split()
maxword=words[0]
minword=words[0]
maxw=words.count(maxword)
minw=words.count(minword)
for word in words:
    num=words.count(word)
    if num>maxw:
        maxw=num
        maxword=word
    if num<minw:
        minw=num
        minword=word
print(maxword,maxw)
print(minword,minw)