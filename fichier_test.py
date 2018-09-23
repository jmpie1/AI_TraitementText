import re
from typing import Any


def classer_text3(file):
    """ Classer les lignes dans un dictionnaire en fonction du nombre de mot"""
    dico = {}
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

    return dico


#classer_text3("ingredients.txt")


def affiche_longeur(text, nb):
    """
    Permet d'afficher les textes commancant par un chiffre et dont le nombre de mot est trois
    :type text: string

    """
    dico={}
    dico = classer_text3(text)

    dico =dico[nb]
    m = 0
    for split_text in dico:
       m += 1
       to_string = split_text[0]+' '+split_text[1]+" "+ split_text[2]

       # pour gérér la ligne avec le mot 'olive,'
       if re.search(r"olive,", to_string):
           to_string1 = to_string.replace(",", "")
           to_string1 = to_string1.split()
           print( "  Résultat: " + to_string1[1] + ', ' + to_string1[0])


       elif re.search(r"vert$|jaune|moyennes$|d’œufs$|thaï$", to_string):
                        print( to_string+ "  Résultat: "+ (split_text[1] + ' ' + split_text[2]).replace(",","") + ', '+ split_text[0])
       elif re.search(r"émincé[s]?$|battu$|écrasés$|tranché$", to_string):

           print(to_string+ "  Résultat: "+ split_text[1] + ', ' + split_text[0])
       elif re.search(r"hamburger$", to_string):
           motif_hambergur = re.compile(r"(?P<quantite>\d \w+)-(?P<produit>\w+ \w+)")
           valeur_motif_ham = motif_hambergur.search(to_string)
           print(to_string+ "  Résultat: "  + valeur_motif_ham.group('produit') + ', '+ valeur_motif_ham.group('quantite'))

       elif re.search(r"petit|grand", to_string):
           motif_pet_grand = re.compile(r"(?P<quantite>\d) (?P<produit>\w+ \w+)")
           valeur_motif_pet_grand = motif_pet_grand.search(to_string)
           print(to_string+ "  Résultat: "  + valeur_motif_pet_grand.group('produit') + ', '+ valeur_motif_pet_grand.group('quantite'))

       else:
           print(to_string+ "  Résultat OUI: "  + split_text[2].replace("d'","").replace("d’","") + ', ' + split_text[0] + ' ' + split_text[1])
    print(m)

if __name__ == "__main__":
    affiche_longeur("ingredients.txt", 3)








