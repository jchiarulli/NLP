import nltk

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

#print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')), '\n')
#print(unusual_words(nltk.corpus.nps_chat.words()), '\n')

from nltk.corpus import stopwords
#print(stopwords.words('english'))

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)

#print(content_fraction(nltk.corpus.reuters.words()))

puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
wordlist = nltk.corpus.words.words()
#print([w for w in wordlist if len(w) >= 6
#       and obligatory in w
#       and nltk.FreqDist(w) <= puzzle_letters])

names = nltk.corpus.names
print(names.fileids())

male_names = names.words('male.txt')
female_names = names.words('female.txt')

#print([w for w in male_names if w in female_names])

cfd = nltk.ConditionalFreqDist(
    (fileid, name[-1])
    for fileid in names.fileids()
    for name in names.words(fileid))

#cfd.plot()
