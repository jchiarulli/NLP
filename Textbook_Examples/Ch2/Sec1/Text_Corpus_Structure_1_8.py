from nltk.corpus import gutenberg

raw = gutenberg.raw('burgess-busterbrown.txt')
print(raw[1:20], '\n')

words = gutenberg.words('burgess-busterbrown.txt')
print(words[1:20], '\n')

sents = gutenberg.sents('burgess-busterbrown.txt')
print(sents[1:20], '\n')
