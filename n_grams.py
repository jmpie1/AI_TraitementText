import nltk
from math import log, exp
# from nltk.util import ngrams
# from collections import Counter

def extraire_n_gramme_probabilite(ligne, len_n_gramme):
    """
    Cette fonction revoie un vecteur contenant des tuples de n-grammes pour calculer la probabilité d'une suite de mot
    :param ligne: string: sequence de mot dont on veut calculer la probabilité
    :param len_n_gramme: la longeur du n-grammme
    :return: liste de n-grammes sous forme de tuples
    """
    if len_n_gramme ==2:
     ligne_token= nltk.word_tokenize("_ "+ligne + " _")   # nous ajoutons des start et end value soit "_"
    elif len_n_gramme == 3:
        ligne_token = nltk.word_tokenize("_ _ " + ligne + " _") # nous ajoutons des start("_ _ ") et end value ("_")
    elif len_n_gramme ==1:
        ligne_token = nltk.word_tokenize(ligne )
    #print(ligne_token)
    n= len(ligne_token)
    lis_n_grammes=[]
    if len_n_gramme ==1:
            for i in range(n):
                #print(ligne_token[i])
                lis_n_grammes.append((ligne_token[i],))
    elif len_n_gramme == 2:
        n1 = n - len_n_gramme + 1
        for i in range(n1 ):
            lis_n_grammes.append(tuple(ligne_token[i:i+len_n_gramme]))
    elif len_n_gramme == 3:
        n1 = n - len_n_gramme + 1
        for i in range( n1):
            lis_n_grammes.append(tuple(ligne_token[i:i + len_n_gramme]))

    return lis_n_grammes
print(extraire_n_gramme_probabilite("This is the cat that killed the rat that ate the malt that lay in the house that Jack built ", 2))

def nb_n_gramme_ligne(ligne_i,n_gram):
    """
    Determine le nombre de fois qu'un n-grammes se trouve dans une ligne données
    :param ligne_i: string: ligne dans laquelle on cherche le n-grammes en question
    :param n_gram: tuple de string: n-grammes que l'on cherche dans la ligne
    :return: entier: nombre d'occurrence du n-gramme
    """
    lis_n_grame=extraire_n_gramme_probabilite(ligne_i, len(n_gram))
    dico ={n_gram:0}
    for i in lis_n_grame:
        if i == n_gram:
            dico[n_gram] +=1
    return dico[n_gram]
#print(nb_n_gramme_ligne("This is the cat that killed the rat that ate the malt that lay in the house that Jack built ", ('is', 'the', 'house')))

def nb_n_gramme_fichier(fichier, n_gram_i):
    """
    Le nombre de fois le n-gramme se trouve dans le corpus
    :param fichier: file: donneés d'entrainemment
    :param n_gram_i: tuple de string
    :return: entier: nombre d'occurence du n-grammes dans le fichier
    """
    with open(fichier, encoding='utf8') as corpus:
        nb_occurence = 0
        for ligne in corpus:
            nb_occurence += nb_n_gramme_ligne(ligne ,n_gram_i)
        return nb_occurence

print("OUII  ", nb_n_gramme_fichier("TestCalcul.txt", ('_', '_')))


def probabilite_n_gramme(data, n_gramme, delta=1):
    """
    Calcule la probabilité d'une conditionnelle d'une séquence
    :param data: fichier: corpus
    :param n_gramme: tuple pour lequel on calcul la probabilité
    :param delta: entier: valeur de lissage
    :return: réel: la probabilité du n-gramme
    """
    valide_start=0
    n = len(n_gramme)
    nb_mot=0
    nb_ligne=0
    with open(data, encoding='utf8') as fichier:
        file_content = fichier.read()
        no_doublon= len(set(nltk.word_tokenize(file_content)))
        nb_mot = len(nltk.word_tokenize(file_content))
    with open(data, encoding='utf8') as fichier:
        while fichier.readline():
            nb_ligne += 1

    if n == 1:
          p = (nb_n_gramme_fichier(data, n_gramme )+ delta)/(nb_mot +delta*no_doublon)
    elif n ==2:
        if n_gramme[:1] == ("_", ):
            valide_start = nb_ligne
        p = (nb_n_gramme_fichier(data, n_gramme) + delta) / (valide_start+nb_n_gramme_fichier(data, n_gramme[:1]) + delta * (no_doublon+nb_ligne))
    elif n ==3:
        print(nb_n_gramme_fichier(data, n_gramme[:2]))
        if n_gramme[:2] == ("_", "_"):
            valide_start = nb_ligne
        p = (nb_n_gramme_fichier(data, n_gramme) + delta) / (valide_start+nb_n_gramme_fichier(data, n_gramme[:2]) + delta * (no_doublon+nb_ligne))

    return  p

print(probabilite_n_gramme("TestCalcul.txt", ('_', '_', 'This')))

def vecteur_probabilite(fichier1, phrase_test, model, smooth=1):
    """
    Elle fournit sous forme de liste les probabilité conditionelles
    :param fichier1: file: corpus
    :param phrase_test:  le phrase de test
    :param model: entier(1 pour unigram, 2 pour bigrammes ..)
    :param smooth: réel ou entier : valeur de lissage
    :return: lis de nombre réel
    """
    lis_prob=[]
    vec_n_gramme_pour_calcul = extraire_n_gramme_probabilite(phrase_test, model)
    print(vec_n_gramme_pour_calcul )
    for i in vec_n_gramme_pour_calcul:
        lis_prob.append(probabilite_n_gramme(fichier1, i, delta=smooth))
    print(lis_prob)
    return lis_prob

vecteur_probabilite("TestCalcul.txt", "This is the house that Jack built",3)

def calcul_log_list_prob(lis):
    """
    Cette fonction calcul le log d'un vecteur de probabilité
    :param lis: liste contenant des probabilités
    :return: liste des log des probabilités
    """
    vec=[log(x) for x in lis]
    print(vec)
    return vec

def prod_prob(lis_log):
    """
    Eplique le fonction inverse du log pour avoir la probabilité
    :param lis_log:
    :return:
    """

    vec = exp(sum(lis_log))

    return  vec


def perplexite(P, n_word):
    """
    Calcul la perplexité
    :param P: La probabilité de la sequence
    :param n_word:  nombre de mot de la ligne de test
    :return: réel: la perplexité
    """
    return 1/((P)**(1/n_word))

print(perplexite(prod_prob(calcul_log_list_prob(vecteur_probabilite("TestCalcul.txt", "This is the house that Jack built",3))),7))