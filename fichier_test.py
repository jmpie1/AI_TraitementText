import re
from typing import Any


def classer_text(file):
    """ Classer les lignes dans un dictionnaire en fonction du nombre de mot"""
    dico = {}
    n2=0
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
           else:

            ma_list = ligne.split()
            if ma_list:
               n2 +=1
               if 100 not in dico.keys():
                  dico[100] = []
                  dico[100].append(ma_list)
               else:
                   dico[100].append(ma_list)
   # print(n2)
    return dico


#classer_text3("ingredients.txt")


def affiche_longeur3(text, nb):
    """
    Permet d'afficher les textes commancant par un chiffre et dont le nombre de mot est trois
    :type text: string
    :type nb: nombre d'élément dans la liste
    """
    dico={}
    dico = classer_text(text)

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
    #print(m)
def affiche_longeur_2(text):
    """
    Permet d'afficher les textes commancant par un chiffre et dont le nombre de mots est trois
    :type text: string

    """
    for ligne in text:
        #split_text = ligne.split()  # type: string
        print(ligne[0] + ', ' + (ligne[1]).replace("d'",""))

def affiche_longeur_4(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " +ligne[3]

        if re.search(r"purée$|échalote[s]?|oignon", my_string) :
            if "française," in ligne:
                print(my_string + " Ingrédients: " + ligne[1] + " " + (ligne[2]).replace(",","") + ', ' + "Quantité: " + ligne[0])
            elif "échalote" in ligne:
                print(my_string + " Ingrédients: " + ligne[2] + ', ' + "Quantité: " + ligne[0]+" " + ligne[1])
            else:
                 print(my_string + " Ingrédients: " + ligne[1] + ', ' + "Quantité: " + ligne[0] )
        elif re.search(r"(\d|½) ((\w+)|(c.à.c)|(c.à.s)) de (\w+)", my_string):
            if ("lime" in ligne):
                 print(my_string + " Ingrédients: " + ligne[1]+" "+ ligne[2] + " "+ ligne[3] + ', ' + "Quantité: " + ligne[0] )
            else:
                 print(my_string + " Ingrédients: "  + ligne[3] + ', ' + "Quantité: " + ligne[0] + " " +ligne[1])
        elif re.search(r"hachée$|d’ail,|saucisses", my_string):
            print(my_string + " Ingrédients: " + ligne[1] + " " +(ligne[2].replace(",","")).replace("d’","")+ ', ' + "Quantité: " + ligne[0] )
        # elif re.search(r"", my_string):

        else:
            print(my_string +" Ingrédients: "+ligne[2].replace("d'","").replace("d’","") + " " +ligne[3] + ', '+ "Quantité: " + ligne[0] + " " +ligne[1])




def affiche100_len_1(len1):
    """ Cette fonction affiche les ligne qui ont um seul mot et ne commanssant pas par un nombre"""
    print("Ingrédients: " + len1[0] + ", " + "Quantité:     ")


def affiche100_len_2(len2):
    """ Cette fonction affiche les ligne qui ont deux mots et ne commanssant pas par un nombre"""
    if "Feuilles" in len2:
        print("Ingrédients: " + (len2[1]).replace("d'", "") + "  " + "Quantité: " + len2[0])
    else:
        print("Ingrédients: " + (len2[0]).replace("des", "") + " " + len2[1] + ", " + "Quantité:     ")

def affiche100_len_3(len3):
    """ Cette fonction affiche les ligne qui ont trois mots et ne commanssant pas par un nombre"""
    if "Préparation" in len3 or "Finition" in len3:
        print(len3[0] + " " + len3[1] + " " + len3[2] + " Ingrédients: " + ",  " + "Quantité:     ")
    elif "pour" in len3 or "du" in len3:
        print(len3[0] + " " + len3[1] + " " + len3[2] + " Ingrédients: " + len3[0] + ", " + "Quantité:     ")
    elif "goût" in len3:
        print(len3[0] + " " + len3[1] + " " + len3[2] + " Ingrédients: " + len3[0] + ", " + "Quantité: " + len3[
            1] + " " + len3[2])
    elif "quelques" in len3:
        print(len3[0] + " " + len3[1] + " " + len3[2] + " Ingrédients: " + len3[2] + ", " + "Quantité: " + len3[
            0] + " " + len3[1])
    elif "Quelques" in len3:
        print(len3[0] + " " + len3[1] + " " + len3[2] + " Ingrédients: " + len3[1] + ", " + "Quantité: " + len3[0])
    elif "Zeste" in len3:
        print(len3[0] + " " + len3[1] + " " + len3[2] + " Ingrédients: " + len3[2] + ", " + "Quantité: " + (
        len3[1]).replace("d'", ""))
    else:
        print(len3[0] + " " + len3[1] + " " + len3[2] + " Ingrédients: " + len3[0] + " " + len3[1] + " " + len3[
            2] + ", " + "Quantité:     ")


def affiche100_len_4(len4):
    """ Cette fonction affiche les ligne qui ont um seul mot et ne commanssant pas par un nombre"""
    if "Quelques" in len4:
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] +
              " Ingrédients: " + len4[3] + ", " + "Quantité: " + len4[0] + " " + len4[1])
    elif "Préparation" in len4:
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] + " Ingrédients: " + ",  " + "Quantité:     ")
    elif "pincée" in len4:
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] + " Ingrédients: " + len4[
            3] + ",  " + "Quantité: " + len4[0] + " " + len4[1])
    elif "sel" in len4:
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] + " Ingrédients: " + len4[1] + " " + len4[
            3] + ",  " + "Quantité: ")
    elif "citron" in len4:
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] + " Ingrédients: " + len4[
            3] + ",  " + "Quantité: " + (len4[2]).replace("d'", ""))
    elif "demi-lime" in len4:
        chaine_lime = (len4[2] + ' ' + len4[3]).split("-")
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] + " Ingrédients: " + chaine_lime[
            1] + ",  " + "Quantité: " + (chaine_lime[0]).replace("d’", ""))
    elif "quinzaine" in len4:
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] + " Ingrédients: " + (len4[2]).replace("d’",
                                                                                                                  "") + ",  " + "Quantité: " +
              len4[0] + " " + len4[1])

    else:
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] +
              " Ingrédients: " + len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] + ", " + "Quantité:     ")

def affiche100_len_5(len5):
    """ Cette fonction affiche les ligne qui ont 5 mots et ne commanssant pas par un nombre"""
    if "Préparation" in len5:
        print(len5[0] + " " + len5[1] + " " + len5[2] + " " + len5[3] + " " + len5[
            4] + " Ingrédients: " + ",  " + "Quantité:     ")
    elif "Feuille" in len5:
        print(len5[0] + " " + len5[1] + " " + len5[2] + " " + len5[3] + " " + len5[4] + " Ingrédients: " + len5[
            2] + ",  " +
              "Quantité: " + len5[0] + " " + len5[3] + " " + len5[4])
    else:
        print(len5[0] + " " + len5[1] + " " + len5[2] + " " + len5[3] + " " + len5[4] + " Ingrédients: " +
              len5[0] + " " + len5[1] + " " + len5[2] + ",  " +
              "Quantité: " + len5[3] + " " + len5[4])

def affiche100_len_6(len6):
    my_string = len6[0] + " " + len6[1] + " " + len6[2] + " " + len6[3] + " " + len6[4] + " " + len6[5]
    if "une" in len6:
        print( my_string + " Ingrédients: " +
              len6[0] + " " + len6[1] + " " + len6[2] + ",  " +  "Quantité: " + len6[4] + " " + len6[5])
    else:
        print(my_string+ " Ingrédients: " + ",  " +
        "Quantité: " )

def affiche100_len_7(len7):
    my_string = len7[0] + " " + len7[1] + " " + len7[2] + " " + len7[3] + " " + len7[4] + " " + len7[5]+ " " + len7[6]
    print(my_string)
    if "moulin" in len7 :
       print( my_string + " Ingrédiant: "+len7[0] + " " + len7[1] + " " + len7[2] + " " + len7[3] + " " + len7[4]
              + ",  " + "Quantité: " + len7[5]+ " " + len7[6])
    else:
        print(my_string + " Ingrédiant: "+ len7[1] + " " + len7[2] + " " + len7[3] + " " + len7[4]+ " " +len7[5]
              + ",  " + "Quantité: "  + len7[0])
def affiche_longeur100(text100):
    ma_liste = classer_text(text100)[100]
    for ligne in  ma_liste:
        lmot = len(ligne)
        if lmot == 1:
            affiche100_len_1(ligne)
        elif lmot == 2:
            affiche100_len_2(ligne)
        elif lmot == 3:
            affiche100_len_3(ligne)
        elif lmot == 4:
            affiche100_len_4(ligne)
        elif lmot == 5:
            affiche100_len_5(ligne)
        elif lmot == 6:
            affiche100_len_6(ligne)
        elif lmot == 7:
            affiche100_len_7(ligne)

if __name__ == "__main__":

    print(classer_text("ingredients.txt")[100])
    Val=classer_text("ingredients.txt")[4]
    #print(len(Val))
    for i in Val:
        #if len(i)==10:
        print (i)
    # affiche_longeur3("ingredients.txt", 3)
    #affiche_longeur100("ingredients.txt")
    # affiche100_len_6(['une', 'petite', 'tasse', 'de', 'riz', 'rond'])

    #affiche100_len_7(['trait', 'jus', 'de', 'citron', 'ou', 'de', 'lime'])
    #affiche_longeur_2(Val)
    affiche_longeur_4(Val)




