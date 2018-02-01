dict = {}
f = open("words.txt", "r")
for line in f.readlines():
    word = line.strip().lower()
    sortedLetters = sorted(list(word))
    sortedWord = "".join(sortedLetters)
    if sortedWord in dict:
        dict[sortedWord].append(word)
    else:
        dict[sortedWord] = [word]

import pickle
with open('words.pickle', 'wb') as f:
    pickle.dump(dict, f)

with open('words.pickle', 'rb') as f:
    dict = pickle.load(f)
