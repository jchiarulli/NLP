from nltk.corpus import genesis

#def lexical_diversity(text):
#    return len(text) / len(set(text))

#def lexical_diversity(my_text_data):
#    word_count = len(my_text_data)
#    vocab_size = len(set(my_text_data))
#    diversity_score = vocab_size / word_count
#    return diversity_score

#kjv = genesis.words('english-kjv.txt')
#print(lexical_diversity(kjv))

def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

#print(plural('fairy'))
#print(plural('woman'))
