from nltk.corpus import PlaintextCorpusReader

corpus_root = '/home/jason/Repo/NLP/Textbook_Examples/Ch2/Corpus_Example'
wordlists = PlaintextCorpusReader(corpus_root, ['a.txt', 'b.txt'])

print(wordlists.fileids())

print(wordlists.words())
