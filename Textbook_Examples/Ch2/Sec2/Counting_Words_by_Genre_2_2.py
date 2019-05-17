import nltk
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))

# Break it down by looking at just two genres.

genre_word = [(genre, word)
              for genre in ['news', 'romance']
              for word in brown.words(categories=genre)]

print(len(genre_word), '\n')

print(genre_word[:4], '\n')    # Beginning of the list genre_word
print(genre_word[-4:], '\n')   # Ending of the list genre_word

cfd = nltk.ConditionalFreqDist(genre_word)

print(cfd, '\n')

print(cfd.conditions(), '\n')

print(cfd['news'], '\n')

print(cfd['romance'], '\n')

print(cfd['romance'].most_common(20), '\n')

print(cfd['romance']['could'], '\n')

print(cfd['romance']['Sunday'])

print(cfd['news']['Sunday'])
