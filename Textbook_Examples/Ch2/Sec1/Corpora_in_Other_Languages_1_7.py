import nltk

#nltk.download('cess_esp')
#nltk.download('floresta')
#nltk.download('indian')
#nltk.download('udhr')

#print(nltk.corpus.cess_esp.words(), '\n')

#print(nltk.corpus.floresta.words(), '\n')

#print(nltk.corpus.indian.words('hindi.pos'), '\n')

#print(nltk.corpus.udhr.fileids(), '\n')

#print(nltk.corpus.udhr.words('Javanese-Latin1')[:11], '\n')

from nltk.corpus import udhr

#languages = ['Chickasaw', 'English', 'German_Deutsch',
#             'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']

#cfd = nltk.ConditionalFreqDist(
#    (lang, len(word))
#    for lang in languages
#    for word in udhr.words(lang + '-Latin1'))

#cfd.plot(cumulative=True)


raw_text = udhr.raw('Italian-Latin1')

nltk.FreqDist(raw_text).plot()
