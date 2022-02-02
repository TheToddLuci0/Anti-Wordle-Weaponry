import json
import argparse


letters = ['q','w','e','t','r','y','u','i','o','p','a','s','d','f','g','h','j'
        ,'k','l','z','x','c','v','b','n','m']
answer = ['8','8','8','8','8']
known = list()
locations = {'0':[], '1':[], '2':[], '3':[], '4':[]}

with open('data/word_data.json','r') as f:
    data = json.loads(f.read())

print('I will give a guess word, you tell me how I did.')
print('For each letter, give me one of the following responses:')
print('c - Valid letter, correct place')
print('v - Valid letter, wrong location')
print('n - Invalid letter')
print('! - Pass this (and only this) to indicate that the word invalid in wordle\n')

count = 1
guess = data.pop(0)['word']

resp = None

while True:
    print(guess)
    key = str(input()).strip()
    if key[0] != '!':
        if len(key) != 5:
            print('Invalid key length')
            continue
        for k in range(0,5):
            if key[k] == 'c':
                answer[k] = guess[k]
            if key[k] == 'v' and guess[k] not in locations[str(k)]:
                locations[str(k)].append(guess[k])
            if key[k] == 'v' or key[k] == 'c':
                if guess[k] not in known:
                    known.append(guess[k])
            if key[k] == 'n':
                try:
                    letters.remove(guess[k])
                    #print(guess[k] + " removed")
                except:
                    # Letter removed already
                    pass
        if '8' not in answer:
            # we won
            print('That took {} guesses.'.format(count))
            exit()
        #print("answer: {}".format(answer))
        #print("letters: {}".format(letters))
        #print("known: {}".format(known))
    else:
        print("Got it, skipping")
        count = count - 1
    guess = None
    while guess == None:
        _guess = data.pop(0)['word']
        abort = False
        if len(known) > 0:
            for i in known:
                if i not in _guess:
                    abort = True
                    #print("Skipping {} because it dones not contain {}".format(_guess, i))
                    break
        if abort:
            continue
        for k in range(0,5):
            if _guess[k] not in letters:
                abort = True
                #print(_guess[k] + " is invalid")
                break
            if answer[k] is not '8' and answer[k] != _guess[k]:
                abort = True
                #print(_guess[k] +" is not " + answer[k])
                break
            if _guess[k] in locations[str(k)]:
                abort = True
                #print(_guess[k] + " is not allowed at this location")
                break
        if abort:
            continue
        guess = _guess
    count += 1
            
