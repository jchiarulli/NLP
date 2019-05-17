import nltk
from nltk.corpus import brown

#print(brown.categories(), '\n')


#print(brown.words(categories='news'), '\n')

#print(brown.words(fileids=['cg22']), '\n')


#print(brown.sents(categories=['news', 'editorial', 'reviews']), '\n')


#news_text = brown.words(categories='news')

#fdist = nltk.FreqDist(w.lower() for w in news_text)

#modals = ['can', 'could', 'may', 'might', 'must', 'will']

#for m in modals:
#    print(m + ':', fdist[m], end=' ')

#print('\n')

#science_fiction_text = brown.words(categories='science_fiction')

#fdist = nltk.FreqDist(w.lower() for w in science_fiction_text)

#modals = ['what', 'when', 'where', 'who', 'why']

#for m in modals:
#    print(m + ':', fdist[m], end=' ')

#print('\n')

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']

cfd.tabulate(conditions=genres, samples=modals)
