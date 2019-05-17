# 3 Computing with Language: Simple Statistics

from nltk.book import *

'''saying = ['After', 'all', 'is', 'said', 'and', 'done',
            'more', 'is', 'said', 'than', 'done']

tokens = set(saying)
print(tokens)

tokens = sorted(tokens)
print(tokens)

print(tokens[-2:])'''

# 3.1 Frequency Distributions

'''fdist1 = FreqDist(text1)
print(fdist1)

print(fdist1.most_common(50))
print(fdist1['whale'])

fdist1.plot(50, cumulative=True)

print(fdist1.hapaxes())'''

# 3.2 Fine-grained Selection of Words

'''V = set(text1)
long_words = [w for w in V if len(w) > 15]
print(sorted(long_words))

fdist5 = FreqDist(text5)
print(sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7))'''

# 3.3 Collocations and Bigrams

'''print(list(bigrams(['more', 'is', 'said', 'than', 'done'])))

print(text4.collocations())
print(text8.collocations())'''

# 3.4 Counting Other Things

#print([len(w) for w in text1])
fdist = FreqDist(len(w) for w in text1)
print(fdist)

print(fdist.most_common())
print(fdist.max())
print(fdist[3])
print(fdist.freq(3))
