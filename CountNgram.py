import nltk
from math import log, exp
from nltk.util import ngrams
from collections import Counter


def count_ngram_sentences1(len_ngram1, sentence1, ngram1):
    """ Cette fonction determine le nombre d'occurence d'un n-gram dans une phrase
    :param len_ngram1: entier : longueur du n-gram
    :param sentence1: string: phrase dans laquelle on va compter le nbre d'occurence du n-grams
    :param ngram1: tuple de string: le n-gram sous forme de tuple
    :return: entier désigant le nombre d'occurence du n-grams
     """
    token_test1 = nltk.word_tokenize(sentence1)
    n_gram_test1 = ngrams(token_test1, len_ngram1)
    return Counter(n_gram_test1)[ngram1]


def count_ngram(len_ngram, train_data, val_ngram):
    """
    Cette fonction détermine le nombre d'occurrence d'un n-grams dans un fichier
    :param len_ngram: nombre de token du n-grams
    :param train_data:  données d'entrainement(dans lequel on cherche le nombre d'occurence du n-grams
    :param val_ngram: n-gram sous forme de tuple
    :return: nb_occurence : entier désigant le nombre d'occurence du n-grams
    """
    with open(train_data, encoding='utf8') as fichier:
      nb_occurence= 0
      for line in fichier:
          nb_occurence += count_ngram_sentences1(len_ngram, line, val_ngram)
      return nb_occurence


def count_all_word(train_data):
    """
    Cette fonction calcule le nombre de tokens(word) dans un fichier
    :param train_data: données d'entrainement
    :return: nombre de tokens dans le fichier
    """
    with open(train_data, encoding='utf8') as fichier:
        file_content = fichier.read()
        word_token=nltk.word_tokenize(file_content)
        return len(word_token)



def add_delta_smooth( train_data):
    """
    Cette fonction calcule le nombre d'unité 'delta'  à ajouter pour le 'smmooth'
    :param train_data: fichier d'entrainement
    :return: entier
    """
    with open(train_data, encoding='utf8') as fichier:
        file_content = fichier.read()
        token_data = nltk.word_tokenize(file_content)
        n= len(set(token_data))
        return n


def calcul_prob(data, n_grams, delta1=0):
    """
    Calcule probabilité d'une suite de mot en fonction du modèle
    :param data: donnée d'entrainement
    :param n_grams: tuple contenant le n-gram
    :param delta1: valeur à ajouter pour le 'smooth'
    :return: réel représentant la probabilité
    """
    V = 0
    n=len(n_grams)
    if n > 1:
        if delta1 != 0:
            V=add_delta_smooth(delta1)
        count_big_ngram = count_ngram(n,data,n_grams)
        count_small_ngram=count_ngram(n-1,data,n_grams[:(n-1)])
        return ((count_big_ngram+delta1)/(count_small_ngram +V))
    else:
        count_big_ngram = count_ngram(n, data, n_grams)
        nb_word=count_all_word(data)
        return ((count_big_ngram+delta1)/(nb_word +V))

print(calcul_prob('TestCalcul.txt', ('do',), delta1=0))

#0.0008000000000000003
def calcul_lis_prob(data_prob, sentence_prob, len_ngram_prob,smoof=0):
    """
    Cette fonction fourni une liste de probabilité pour une suite  de mots
    :param data_prob: données d'entrainement
    :param sentence_prob: suite de mots dont on veut la probabilité
    :param len_ngram_prob: longeur du n-gram en fonction du modèle
    :param smoof: paramètre de lissage
    :return: liste de probabilité
    """
    lis_prob=[]
    lis_prob.append(calcul_prob(data_prob, (sentence_prob.split()[0],), smoof))
    token_test_prob = nltk.word_tokenize(sentence_prob)
    n_gram_test_prob = ngrams(token_test_prob, len_ngram_prob)
    for tup in n_gram_test_prob:
        lis_prob.append(calcul_prob(data_prob,tup,smoof))
        #print(calcul_prob(data_prob,tup,smoof))
    return lis_prob

def calcul_log_list(lis):
    """
    Cette fonction calcul le log d'un vecteur de probabilité
    :param lis: liste contenant des probabilités
    :return: liste des log des probabilités
    """
    return [log(x) for x in lis]
print(calcul_lis_prob('TestCalcul.txt', '_ I do like Sam I am __',2))

#[0.2, 0.2, 0.5, 0.3333333333333333, 0.6, 0.4, 0.5]
def trouve_proba(lis):
    """
    Fourni la probabilité en utilisant la fonction inverse du log
    :param lis: liste des log des probabilités
    :return: réel représentant la probabilité
    """
    return exp(sum(lis))

def trouve_perplexite_mod(p, N):
    """
    Calcul la perplexité du modèle
    :param p: réel représantant la probabilité
    :param N: entier représentant le nombre de mots
    :return:
    """
    return 1/((p)**(1/N))
# print(add_delta_smooth(1, 'proverbes.txt'))
# #print(count_ngram(2,'_ Sam I do I do like _', ('I','do')))
# # print (Counter(bigrams).items())
# #print(Counter(bigrams)[('_', 'Sam')])
# token = nltk.word_tokenize('_ Sam I do I do like _')
# bigrams= ngrams(token,2)
# dico= Counter(bigrams)
# for k in dico:
#     print(dico[k])

