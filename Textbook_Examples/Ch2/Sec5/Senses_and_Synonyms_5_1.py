from nltk.corpus import wordnet as wn

#print(wn.synsets('motorcar'), '\n')

#print(wn.synset('car.n.01').lemma_names(), '\n')

#print(wn.synset('car.n.01').definition(), '\n')
#print(wn.synset('car.n.01').examples(), '\n')

#print(wn.synset('car.n.01').lemmas(), '\n')
#print(wn.lemma('car.n.01.automobile'), '\n')
#print(wn.lemma('car.n.01.automobile').synset(), '\n')
#print(wn.lemma('car.n.01.automobile').name(), '\n')

#print(wn.synsets('car'))

#for synset in wn.synsets('car'):
#    print(synset.lemma_names())

#print(wn.lemmas('car'))

print(wn.synsets('motorcar'), '\n')

print(wn.synset('car.n.01').lemma_names(), '\n')

print(wn.synset('car.n.01').definition(), '\n')
print(wn.synset('car.n.01').examples(), '\n')

print(wn.synset('car.n.01').lemmas(), '\n')
print(wn.lemma('car.n.01.automobile'), '\n')
print(wn.lemma('car.n.01.automobile').synset(), '\n')
print(wn.lemma('car.n.01.automobile').name(), '\n')

print(wn.synsets('car'))

for synset in wn.synsets('car'):
    print(synset.lemma_names())

print(wn.lemmas('car'))
