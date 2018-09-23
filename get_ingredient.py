import re
from typing import Any


def classer_text(file):
    """ Classer les textes dans un dictionnaire en fonction du nombre de mot"""
    dico = dict()
    with open(file,encoding='utf8') as fichier:
        m = 0
        for ligne in fichier:
           m += 1
           if ligne[0].isnumeric():
                ma_list = ligne.split()
                n = len(ma_list)
                if n not in dico.keys():
                    dico[n]= []
                    dico[n].append(ma_list)
                else:
                    dico[n].append(ma_list)
    #print(m)
    print(dico)
classer_text("ingredients.txt")

def affiche_longeur_3(text):
    """
    Permet d'afficher les textes commancant par un chiffre et dont le nombre de mot est trois
    :type text: string

    """

    if text[0].isnumeric():
        split_text = text.split()  # type: string
        if len(split_text) == 3:
            if re.match(r"(\w+) (\w+) (\w+)", text) is None:
                # m1 = re.match(r"(\w+) (\w+) (\w+)", text)
                print(split_text[0] + ' ' + split_text[1] + ', ' + split_text[2])
            else:
                print(split_text[0] + ' ' + split_text[1] + ', ' + split_text[2])
        if len(split_text) == 2:
            print(split_text[0] + ', ' + split_text[1])
    else:

        pass


def affiche_longeur_2(text):
    """
    Permet d'afficher les textes commancant par un chiffre et dont le nombre de mots est trois
    :type text: string

    """

    if text[0].isnumeric():
        split_text = text.split()  # type: string
        if len(split_text) == 2:
            print(split_text[0] + ', ' + split_text[1])
    else:

        pass
