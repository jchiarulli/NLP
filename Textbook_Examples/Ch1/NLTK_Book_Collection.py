from nltk.book import *

#text1

#text2

# 1.3 Searching Text

'''text1.concordance("monstrous")
print("\n")

text3.concordance("truth")
print("\n")

text6.concordance("chipper")
print("\n")

# Determines what other words appear in a similar range of contexts
text1.similar("monstrous")
print("\n")

text2.similar("monstrous")
print("\n")

# Contexts shared by two or more words
text2.common_contexts(["monstrous", "very"])
print("\n")

text3.similar("create")
print("\n")

text4.common_contexts(["right", "country", "wrong"])
print("\n")

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])'''

# 1.4 Counting Vocabulary

'''print(len(text3))

print(set(text3))

print(sorted(set(text3)))

print(len(set(text3)))'''

'''print(len(set(text3))/len(text3))

print(text3.count("smote"))

print(100 * text4.count('a') / len(text4))'''

'''print(text5.count("lol"))

print(100 * text5.count('lol') / len(text5))'''

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

lexical_diversity(text3)
lexical_diversity(text5)

percentage(4, 5)

percentage(text4.count('a'), len(text4))
