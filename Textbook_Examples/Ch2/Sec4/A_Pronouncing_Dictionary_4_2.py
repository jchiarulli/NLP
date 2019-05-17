import nltk

entries = nltk.corpus.cmudict.entries()
#print(len(entries))

#for entry in entries[42371:42379]:
#    print(entry)

#for word, pron in entries:
#    if len(pron) == 3:
#        ph1, ph2, ph3 = pron
#        if ph1 == 'P' and ph3 == 'T':
#            print(word, ph2, end=' ')

#print('\n')

syllable = ['N', 'IH0', 'K', 'S']
#print([word for word, pron in entries if pron[-4:] == syllable])

#print([w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n'], '\n')
#print(sorted(set(w[:2] for w, pron in entries if pron[0] == 'N' and w[0] != 'n')))

def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]

#print([w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']], '\n')
#print([w for w, pron in entries if stress(pron) == ['0', '2', '0', '1', '0']])

p3 = [(pron[0] + '-' + pron[2], word)
      for (word, pron) in entries
      if pron[0] == 'P' and len(pron) == 3]

cfd = nltk.ConditionalFreqDist(p3)

for template in sorted(cfd.conditions()):
    if len(cfd[template]) > 10:
        words = sorted(cfd[template])
        wordstring = ' '.join(words)
        print(template, wordstring[:70] + "...")

print('\n')

prondict = nltk.corpus.cmudict.dict()
#print(prondict['fire'])

# Causes an error since the wordblog is missing from the pronouncing dictionary
#print(prondict['blog'])

prondict['blog'] = [['B', 'L', 'AA1', 'G']]
#print(prondict['blog'])

text = ['natural', 'language', 'processing']
print([ph for w in text for ph in prondict[w][0]])
