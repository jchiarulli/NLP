#import nltk
#from nltk.corpus import inaugural

#cfd = nltk.ConditionalFreqDist(
#    (target, fileid[:4])
#    for fileid in inaugural.fileids()
#    for w in inaugural.words(fileid)
#    for target in ['america', 'citizen']
#    if w.lower().startswith(target))

#from nltk.corpus import udhr

#languages = ['Chickasaw', 'English', 'German_Deutsch',
#             'Greenlandic_Inuktikut', 'Hungarian_Magyar',
#             'Ibibio_Efik']

#cfd = nltk.ConditionalFreqDist(
#    (lang, len(word))
#    for lang in languages
#    for word in udhr.words(lang+ '-Latin1'))

#cfd.tabulate(conditions=['English', 'German_Deutsch'],
#             samples=range(10), cumulative=True)

import nltk
from nltk.corpus import brown

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday']

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in ['news', 'romance']
    for word in brown.words(categories=genre))

cfd.tabulate(samples=days)
cfd.plot(samples=days)
