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


def affiche_longeur3(text3, nb):
    """
    Permet d'afficher les textes commancant par un chiffre et dont le nombre de mot est trois
    :type text: string
    :type nb: nombre d'élément dans la liste
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
    #print(m)


def affiche_longeur100(text100):
    ma_liste = classer_text(text100)[100]
    for ligne in  ma_liste:
      if len(ligne) == 5:
        lmot = len(ligne)
        if lmot == 1:
            print("Ingrédients: " +ligne[0] + ", "+ "Quantité:     ")

        elif lmot == 2:
            if "Feuilles" in ligne:
                print("Ingrédients: " + (ligne[1]).replace("d'", "")+ "  " +"Quantité: " +ligne[0] )
            else:
                 print("Ingrédients: " + (ligne[0]).replace("des", "") +" "+ ligne[1] +", " + "Quantité:     ")
        elif lmot == 3:
            if "Préparation" in ligne or "Finition" in ligne:
                print(ligne[0] + " " + ligne[1] + " " + ligne[2] +" Ingrédients: " + ",  " + "Quantité:     ")
            elif "pour" in ligne or "du" in ligne  :
                print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " Ingrédients: " + ligne[0] + ", " + "Quantité:     ")
            elif "goût" in ligne:
                print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " Ingrédients: " + ligne[0] + ", " + "Quantité: " +ligne[1] + " " + ligne[2])
            elif "quelques" in ligne:
                print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " Ingrédients: " + ligne[2] + ", " + "Quantité: " + ligne[0] + " " + ligne[1])
            elif "Quelques" in ligne:
                print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " Ingrédients: " + ligne[1] + ", " + "Quantité: " + ligne[0] )
            elif "Zeste" in ligne:
                print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " Ingrédients: " + ligne[2] + ", " + "Quantité: " + (ligne[1]).replace("d'","") )
            else:
                print(ligne[0]+" " +ligne[1]+" " +ligne[2] +" Ingrédients: " + ligne[0]+ " "+ligne[1]+ " " + ligne[2] + ", " + "Quantité:     ")
        if len(ligne) == 4:
          if "Quelques" in ligne:
              print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] +
                    " Ingrédients: "  + ligne[3] + ", " + "Quantité: " + ligne[0] + " " + ligne[1])
          elif "Préparation"  in ligne:
                  print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] +" Ingrédients: " + ",  " + "Quantité:     ")
          elif "pincée"  in ligne:
                  print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] +" Ingrédients: " + ligne[3]+ ",  " + "Quantité: " +ligne[0] + " " + ligne[1])
          elif "sel"  in ligne:
             print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] +" Ingrédients: " +ligne[1] + " " + ligne[3]+ ",  " + "Quantité: "  )
          elif "citron"  in ligne:
             print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] +" Ingrédients: " +ligne[3] + ",  " + "Quantité: "+(ligne[2]).replace("d'",""))
          elif "demi-lime"  in ligne:
            chaine_lime= (ligne[2]+' '+ligne[3]).split("-")
            print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] +" Ingrédients: " +chaine_lime[1] + ",  " + "Quantité: "+(chaine_lime[0]).replace("d’",""))
          elif "quinzaine"  in ligne:
            print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] +" Ingrédients: " +(ligne[2]).replace("d’", "") + ",  " + "Quantité: "+ligne[0] +" "+ligne[1])

          else:
             print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] +
                " Ingrédients: " + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] + ", " + "Quantité:     ")
      if len(ligne) == 5:
          if "Préparation"  in ligne:
                  print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] + " " + ligne[4] +" Ingrédients: " + ",  " + "Quantité:     ")
          elif "Feuille"  in ligne:
                  print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] + " " + ligne[4] +" Ingrédients: " + ligne[2]+ ",  " +
                        "Quantité: "+ligne[0]+ " " + ligne[3] + " " + ligne[4])
          else:
              print(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] + " " + ligne[4] + " Ingrédients: " +
                    ligne[0] + " " +ligne[1] + " " + ligne[2]+",  " +
                    "Quantité: " + ligne[3]+" " + ligne[4])

if __name__ == "__main__":
    print(classer_text("ingredients.txt")[100])
    #affiche_longeur("ingredients.txt", 3)
    affiche_longeur100("ingredients.txt")








