from nltk.book import *
from NLTK_Book_Collection import lexical_diversity

# 2.1 Lists

'''sent1 = ['Call', 'me', 'Ishmael', '.']

print(len(sent1))

print(lexical_diversity(sent1))

sent2 = ['The', 'family', 'of', 'Dashwood', 'had', 'long', 'been', 'settled', 'in', 'Sussex', '.']

sent3 = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and', 'the', 'earth', '.']

print(['Monty', 'Python'] + ['and', 'the', 'Holy', 'Grail'])

sent4 = ['Fellow', '-', 'Citizens', 'of', 'the', 'Senate', 'and', 'of', 'the',
        'House', 'of', 'Representatives', ':']

print(sent4 + sent1)

sent1.append('Some')
print(sent1)'''

# 2.2 Indexing Lists

'''print(text4[173])

print(text4.index('awaken'))

print(text5[16715:16735])
print(text6[1600:1625])

sent = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 
        'word10']

print(sent[0])
print(sent[9])

print(sent[5:8])
print(sent[5])
print(sent[6])
print(sent[7])

print(sent[:3]) 
print(text2[141525:])

sent[0] = 'First'
print(sent[0])
sent[9] = 'Last'
print(sent[9])

print(len(sent))

sent[1:9] = ['Second', 'Third']
print(sent)'''

#print(sent[9])     # Error: list now has only four elements

# 2.3 Variables

'''my_sent = ['Bravely', 'bold', 'Sir', 'Robin', ',', 'rode',
        'forth', 'from', 'Camelot', '.']

noun_phrase = my_sent[1:4]
print(noun_phrase)

wOrDs = sorted(noun_phrase)
print(wOrDs)

vocab = set(text1)
vocab_size = len(vocab)
print(vocab_size)'''

# 2.4 Strings

name = 'Monty'
print(name[0])

print(name[:4])

print(name * 2)
print(name + '!')

print(' '.join(['Monty', 'Python']))
print('Monty Python'.split())
