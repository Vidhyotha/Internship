text=input('enter a sentence: ')
text=text.lower()
words=text.split()
uwords={}
for word in words:
    if word not in uwords:
        count=words.count(word)
        uwords[word]=count
print('Number of unique words: ',len(uwords))
for word in uwords:
    print(word,': ',uwords[word])