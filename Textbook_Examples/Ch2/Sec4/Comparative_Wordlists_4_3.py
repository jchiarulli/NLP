from nltk.corpus import swadesh

print(swadesh.fileids(), '\n')
print(swadesh.words('en'), '\n')

fr2en = swadesh.entries(['fr', 'en'])
print(fr2en, '\n')

translate = dict(fr2en)
print(translate['chien'])
print(translate['jeter'], '\n')

de2en = swadesh.entries(['de', 'en'])   # German-English
es2en = swadesh.entries(['es', 'en'])   # Spanish-English

translate.update(dict(de2en))
translate.update(dict(es2en))

print(translate['Hund'])
print(translate['perro'], '\n')

languages = ['en', 'de', 'nl', 'es', 'fr', 'pt', 'la']

for i in [139, 140, 141, 142]:
    print(swadesh.entries(languages)[i])
