import re
from collections import Counter

with open('C:\\Users\\User\\Downloads\\Book.txt', 'r') as file:

    textHandler = file.read()
    findWord = r'\w{1,20}'
    count = Counter()
    text = re.findall(findWord, textHandler)
    text.sort()

    for word in text:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

for word in count:
    print(word.ljust(25), count[word])
