word=input('Enter word: ')
vowels=[]
for letter in word:
    if letter in 'aeiou':
        vowels+=letter
print(vowels,len(vowels))