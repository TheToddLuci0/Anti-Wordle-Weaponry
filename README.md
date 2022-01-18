# Anti Wordle Weaponry
I'm the kind of person who sees a cool puzzle and thinks "I wonder if I can 
solve that". Of course, that's usually followed by "I wonder if I can get 
python to solve that faster".

Thus, Anti Wordle Weaponry was born. A great way to remove any enjoyment from a 
fun brain teaser. The original game can be found 
[here](https://www.powerlanguage.co.uk/wordle/)

### How the words are chosen
First, get a list of all words from [NTLK](https://pypi.org/project/nltk/).

Second, remove all words that aren't five letters in length.

Finally, calculate a weighted score. Currently, that's done by multiplying the
frequency of each letter in each word by the 'uniqueness' of the word.
For example, 'apple' has a raw score of `16267`, and weighted score of 
`13013.6`. The weighted score will only ever be lower, because we multiply by
`uniq/5`, which in the case of apple is `4/5`. 

All of the above is done ahead of time using 
[generate\_data.py](/data/generate_data.py), because it's resource intensive,
and dosen't change particulatly often.

Using this data, we can then make inteligent guesses by using the highest
weighted word that fits the current game state.
