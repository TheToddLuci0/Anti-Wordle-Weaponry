import nltk
import json
from nltk.corpus import words


# Grab a list of all english words
nltk.download('words')

fives = list()

for w in words.words():
    if len(w) == 5:
        fives.append(w.lower())

letters = {'a': 0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,
        'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,
        'w':0,'x':0,'y':0,'z':0}

for w in fives:
    for key in letters.keys():
        letters[key] += w.count(key)

weighted = list()

while len(fives) != 0:
    w = fives.pop()
    uniques = 0
    points = 0
    for k in letters.keys():
        count = w.count(k)
        if count > 0:
            uniques += 1
            points += count * letters[k]
    weight = points * (uniques/5)
    weighted.append({'word':w, 'raw':points, 'weighted':weight})

with open('word_data.json','w') as f:
    json.dump(sorted(weighted, key = lambda i: i['weighted'], reverse=True), f)
with open('letter_data.json','w') as f:
    json.dump(letters, f)
