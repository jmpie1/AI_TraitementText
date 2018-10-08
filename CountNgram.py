import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

text = "I need to write a program in NLTK that breaks a corpus (a large collection of \
txt files) into unigrams, bigrams, trigrams, fourgrams and fivegrams. I need to write a program in NLTK that breaks a corpus"

def count_ngram(len_ngram, train_data, val_ngram):
  token_test = nltk.word_tokenize(train_data)
  print(set(token_test))
  print(len(set(token_test)))
  n_gram_test = ngrams(token_test,len_ngram)
  return Counter(n_gram_test)[val_ngram]

def add_delta_smooth(delta, train_data, deno=True):
    with open(train_data, encoding='utf8') as fichier:
        file_content = fichier.read()
        token_data = nltk.word_tokenize(file_content)
        n= len(set(token_data))
        if deno:
           return n
        else:
           return delta


print(add_delta_smooth(1, 'proverbes.txt'))
#print(count_ngram(2,'_ Sam I do I do like _', ('I','do')))
# print (Counter(bigrams).items())
#print(Counter(bigrams)[('_', 'Sam')])
token = nltk.word_tokenize('_ Sam I do I do like _')
bigrams= ngrams(token,2)
dico= Counter(bigrams)
for k in dico:
    print(dico[k])

