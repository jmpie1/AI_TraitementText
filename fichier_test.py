import re


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
           print( ' "{0}", "{1}"'.format(to_string1[1] , to_string1[0]))


       elif re.search(r"vert$|jaune|moyennes$|d’œufs$|thaï$", to_string):
           print(' "{0}", "{1}"'.format((split_text[1] + ' ' + split_text[2]).replace(",",""), split_text[0]))
       elif re.search(r"émincé[s]?$|battu$|écrasés$|tranché$", to_string):

           print(' "{0}", "{1}"'.format(split_text[1] , split_text[0]))
       elif re.search(r"hamburger$", to_string):
           motif_hambergur = re.compile(r"(?P<quantite>\d \w+)-(?P<produit>\w+ \w+)")
           valeur_motif_ham = motif_hambergur.search(to_string)
           print(' "{0}", "{1}"'.format(valeur_motif_ham.group('produit'), valeur_motif_ham.group('quantite')))
       elif re.search(r"petit|grand", to_string):
           motif_pet_grand = re.compile(r"(?P<quantite>\d) (?P<produit>\w+ \w+)")
           valeur_motif_pet_grand = motif_pet_grand.search(to_string)
           #print(to_string+ "  Résultat: "  + valeur_motif_pet_grand.group('produit') + ', '+ valeur_motif_pet_grand.group('quantite'))
           print(' "{0}", "{1}"'.format(valeur_motif_pet_grand.group('produit'), valeur_motif_pet_grand.group('quantite')))
       else:
           #print(to_string+ "  Résultat OUI: "  + split_text[2].replace("d'","").replace("d’","") + ', ' + split_text[0] + ' ' + split_text[1])
           print(' "{0}", "{1}"'.format(split_text[2].replace("d'","").replace("d’",""),split_text[0] + ' ' + split_text[1] ))
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
            if re.search("française,", my_string):
                print(my_string + " Ingrédients: " + ligne[1] + " " + (ligne[2]).replace(",","") + ', ' + "Quantité: " + ligne[0])
            elif re.search(r"échalote", my_string):
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


def affiche_longeur_5(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]
        if re.search(r"\d (\w+) de (\w+) (\w+)", my_string):
               if "noix" == ligne[1]:
                   print(my_string + " Ingrédients: " + ligne[3] +', ' + "Quantité: " + ligne[0] + " " + ligne[1])
               else:
                   print(my_string + " Ingrédients: " + ligne[3] + " " + ligne[4] + ', ' + "Quantité: " + ligne[0] + " "+ligne[1])
        elif  re.search(r"café|(c. à .s)",my_string):
            print(my_string + " Ingrédients: " + ligne[0] + " " + ligne[1]+ " "+ligne[3]  + ', ' + "Quantité: " + ligne[4].replace("d’",""))
        elif re.search(r"sauce",my_string):
            print(my_string + " Ingrédients: " + " " + ligne[3] + " " + ligne[4] + ', ' + "Quantité: " + ligne[0] + " " + ligne[1])
        elif "cheddar" == ligne[3]:
            print(my_string + " Ingrédients: " + ligne[2] + " " + ligne[3] + ', ' + "Quantité: " + ligne[0]+ " " +ligne[1]  )
        elif re.search(r"\d petit oignon",my_string):
            print(my_string + " Ingrédients: " + ligne[1] + " " + ligne[2] + " " + ligne[3] + ', ' + "Quantité: " + ligne[0])
        elif "farine" == ligne[4]:
            print(my_string + " Ingrédients: " + ligne[0] + " " + ligne[1] + " " + ligne[2] + ', ' + "Quantité: " +ligne[4])
        elif re.search(r"Kg$",my_string):
            print(my_string + " Ingrédients: " + ligne[1]+', ' + "Quantité: " + ligne[0]+ " (" + ligne[3]+ligne[4]+ ")")
        else:
            print(my_string + " Ingrédients: " + (ligne[2].replace("d’","") + " "+ligne[3] + " " + ligne[4] + ', ' + "Quantité: " + ligne[0] + " "+ligne[1]))


def affiche_longeur_6(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]
        if re.search(r"\d (c.) (à) (\w+) de (\w+)", my_string) or "bicarbonate" in ligne:
            print(my_string + " Ingrédients: " + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ ', ' + "Quantité: " + ligne[5])
        elif  re.search(r"(\d+|\d) (\w+) (de) (\w+) (\w+) (\w+)", my_string):
            if "congre" in ligne:
                print(my_string + " Ingrédients: " + ligne[0] + " " + ligne[ 1] + " ("+ligne[ 4]+ ligne[ 5]+ ")"+', ' + "Quantité: " + " " + ligne[3])
            else:
                print(my_string + " Ingrédients: " + ligne[0]  +" " + ligne[1]+ ', ' + "Quantité: " +" " + ligne[3] + " " + ligne[4] +" " +ligne[5])
        elif re.search(r"(\()", my_string):
             print(my_string +" Ingrédients: " + (ligne[4]).replace("d’","")  +" " + ligne[5]+ ', '+ "Quantité: " + ligne[0] + " " + ligne[ 1] + " "+ligne[ 2]+ " "+ligne[ 3])

        elif re.search(r"(c.à.s)", my_string):
             print(my_string + " Ingrédients: " + ligne[0] + " " + ligne[1] + ', ' + "Quantité: " + ligne[3] + " " + ligne[4]+" " + ligne[5])

        elif re.search(r"décorer$", my_string):
            print(my_string + " Ingrédients: " + ligne[0] + " " + ligne[1] + ', ' + "Quantité: " + (ligne[3]).replace(",","") )
        elif re.search(r"pommes", my_string):
            print(my_string + " Ingrédients: " + ligne[0]+', ' + "Quantité: " + ligne[1] + " " + ligne[2] )

        elif re.search(r"pièce", my_string):
            print(my_string + " bbbb Ingrédients: " + ligne[3] + ', ' + "Quantité: " +  ligne[0] + " " + ligne[1]
                  + " " +"("+ligne[4].replace("d'","")+" "+ligne[5]+")" )

        else:
            print(my_string + " bbbb Ingrédients: " + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] + ', ' + "Quantité: " + ligne[5])




def affiche_longeur_7(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " + ligne[6]

        if re.search( r"((ml\))|(g\))|(soupe\)))",ligne[5]):
            print(my_string + " Ingrédients: " + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " +
                  ligne[3] + " "+ ligne[4] + " " + ligne[5] + ", " + "Quantité: " + ligne[6].replace("d’",""))
        elif re.search( r"(claire$|foncée$|frisé$|Paris$|verts$)",ligne[6]):
            print(my_string + " Ingrédients: " + ligne[3] + " " + ligne[4] + " " + ligne[5] + " " +
                  ligne[6] + ", " + "Quantité: " + ligne[0] + " " + ligne[1])

        elif re.search( r"(blanc$|fraîche$|râpé$|moulue$|César$|séché$|balsamique$|pla$)",ligne[6]):
            if "rhum"== ligne[5] or "nam"== ligne[5]:
                print(my_string + " Ingrédients: " + ligne[5] + " " +
                      ligne[6] + ", " + "Quantité: " + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4])
            else:
              print(my_string + " Ingrédients: " + ligne[5] + " " +
                  ligne[6] + ", " + "Quantité: " + ligne[0] + " " + ligne[1]+ " " + ligne[2] + " " + ligne[3])
        elif re.search( r"(purée$)",ligne[6]):
            print(my_string + " Ingrédients: " + ligne[2] + " " + ligne[3] + " " +
                  ligne[4] + ", " + "Quantité: " + ligne[0] + " " + ligne[1] )
        elif re.search( r"(rawit)",ligne[6]):
            print(my_string + " Ingrédients: " + ligne[1] + " " + ligne[2] + " " +ligne[3]+ " " + ligne[4]+
                  " " +ligne[5] + " " + ligne[6]+", " + "Quantité: " + ligne[0] )
        elif re.search( r"rincées$",ligne[6]):
            print(my_string + " Ingrédients: " + ligne[1] + " " + ligne[2] +", " + "Quantité: " + ligne[0] )

        elif re.search( r"g$",ligne[6]):
            print(my_string + " Ingrédients: " + ligne[3] +", " +
                  "Quantité: " + ligne[0]+" " +ligne[1] + " (" + ligne[5] + " " +ligne[6]+")" )
        else:
          print(my_string + " Ingrédients: " + (ligne[4]).replace("d’","") + " " + ligne[5] + " " + ligne[6]+ ", "  + "Quantité: "
              + ligne[0]+  " "+ligne[1] + " " + ligne[2]+ " " + ligne[3])

def affiche_longeur_8(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]
        if re.search(r"râpé$", ligne[7]):
            print(my_string + "1111111111 Ingredients: " +  ligne[6] + ", " + "Quantité: "
                  + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4] + " " + ligne[5])
        elif re.search(r"(goût$)", ligne[7]):
            print(my_string + " 22222222Ingredients: " +  ligne[4] + ", " + "Quantité: "
                  + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[5] + " " + ligne[6]+" " + ligne[7])
        elif re.search(r"(blanc$|soya$|d’olive$)", ligne[7]):
            print(my_string + "Ingredients: " + ligne[6].replace("d’","")+" " + ligne[7] + ", " + "Quantité: "
                  + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4] + " "+ligne[5] )
        elif re.search(r"(safran$)", ligne[7]):
            print(my_string + " Ingredients: " + ligne[7] + ", " + "Quantité: "
                  + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4] + " "+ligne[5] )
        elif re.search(r"(deux$)", ligne[7]):
            print(my_string + "Ingredients: " + ligne[2][2:5].replace("d’","") + ", " + "Quantité: "
                  + ligne[0] + " " + ligne[1] )
        elif re.search(r"(d'érable$)", ligne[7]):
            print(my_string + " Ingredients: " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7] + ", " + "Quantité: "
                  + ligne[0] + " " + ligne[1] )

        else:
           print(my_string + "Ingredients: " +ligne[5] + " " + ligne[6] + " " + ligne[7]+ ", "  + "Quantité: "
              + ligne[0]+  " "+ligne[1] + " " + ligne[2]+ " " + ligne[3] )


def affiche_longeur_9(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]+" " + ligne[8]
        if re.search(r"(biseaux$arachide)",ligne[8]):
            print(my_string + " Ingredients: " + ligne[4] + " " + ligne[5]  + ", " + "Quantité: "
                  + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] )

        elif re.search(r"(arachide$)",ligne[8]):
            print(my_string + " Ingredients: " + ligne[4].replace("d’", "") + " " + ligne[5]+" "+ ligne[6]+" " + ligne[7]+" " + ligne[8] + ", " + "Quantité: "
                  + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] )

        elif re.search(r"(nettoyées$)",ligne[8]):
            print(my_string + " Ingredients: " + ligne[5].replace(",", "") + ", " + "Quantité: "
                  + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] )
        elif re.search(r"(l’eau$)",ligne[8]):
            print(my_string + " Ingredients: " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]+" " + ligne[8] +", " + "Quantité: "
                  + ligne[0] + " " + ligne[1] )
        elif re.search(r"(dorées$)",ligne[8]):
            print(my_string + " Ingredients: " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]+" " + ligne[8] +", " + "Quantité: "
                  + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3])

        else:
           print(my_string +" Ingredients: " +ligne[6] + " " + ligne[7] + " " + ligne[8]+ ", "  + "Quantité: "
              + ligne[0]+  " "+ligne[1] + " " + ligne[2]+ " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5])



def affiche_longeur_10(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]+" " + ligne[8]+" " + ligne[9]
        if re.search(r"(égoutté[e]?s$)",my_string):
            print(my_string + "Quantité: " + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]
                  + ", " + "Ingrédiant: " + ligne[5]+ " " +\
                    ligne[6]+"" +(ligne[7] + " " + ligne[8]).replace("rincés et",""))
        elif re.search(r"(râpé$)",my_string):
            print(my_string + "Quantité: " + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]
                  +  " " + ligne[4]+ " " + ligne[5]+", " + "Ingrédiant: " + ligne[7])
        elif re.search(r"(beurre,)",my_string):
            print(my_string + "Quantité: " + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]
                  +  " " + ligne[4]+ " " + ligne[5]+" " + ligne[9]+", " + "Ingrédiant: " + ligne[7])

        elif re.search(r"(secs)", my_string):
            print(my_string + "Quantité: " + ligne[0] + " " + ligne[1] + ", " + "Ingrédiant: " + ligne[3] +" "+ ligne[4] +" "+ ligne[5])
        else:

           print(my_string +
                 " Quantités: " +ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6].replace("de","") +" , " +"Ingrédients: "+ ligne[7].replace("d’","")+" " + ligne[8]+ ", ")

def affiche_longeur_11(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]+" " + ligne[8]+" " + ligne[9]+" "+ligne[10]

        if re.search(r"(morceaux)",my_string):

           print(my_string + " Quantités: " + ligne[0] + " " + ligne[1] + " , " + "Ingrédients: " + ligne[2] + " " + ligne[3]
                 + " " + ligne[4])
        elif re.search(r"(blanc)",my_string):

           print(my_string + " Quantités: " + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " , " + "Ingrédients: " + ligne[7] + " " + ligne[8]
                 + " " + ligne[9]+ " " + ligne[10])

        elif re.search(r"(langoustines|tomates)",my_string):

           print(my_string + " Quantités: " + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]
                 + " , " + "Ingrédients: " + ligne[5] + " " + ligne[6]
                 + " " + (ligne[7].replace(",","")).replace("et",""))
        elif re.search(r"(pain)",my_string):

           print(my_string + " Quantités: " + ligne[0] + " " + ligne[1] + " , " + "Ingrédients: " + ligne[3] + " " + ligne[4])

        elif re.search(r"(coriandre)",my_string):

           print(my_string + " Quantités: " + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]
                 + " , " + "Ingrédients: " + ligne[5] + " ou " + ligne[10])

        elif re.search(r"(moulu)",my_string):

           print(my_string + " Quantités: " + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]
                 + " " + ligne[5]+ " , " + "Ingrédients: " + ligne[7] + " ou " + ligne[8])

        else:

           print(my_string +  " Quantités: " +ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]
              +" , " +"Ingrédients: "+ ligne[4].replace("d’","")+" " + ligne[5])

def affiche_longeur_12(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]+" " + ligne[8]+" " + ligne[9]+" "+ligne[10]+" "+ligne[11]

        if re.search(r"(concassés$)",my_string):
            print(ligne[7]+" " + ligne[8]+" " + ligne[9]+" "+ligne[10]+ ", "+ ligne[0] + " " + ligne[1] + " "
                  + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5])
        else:
            print( '"'+ligne[1] + " "+ ligne[2].replace(",","")+'"' + ", " + ligne[0] )

def affiche_longeur_14(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]+" " + ligne[8]+" " + ligne[9]+" "+ligne[10]+" "+ligne[11]+" "+ligne[12]\
                    +" " + ligne[13]
        print('"' + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] + '"' + ", " + ligne[4][2:]+ " " + ligne[5])


def affiche_longeur_16(text):
    for ligne in text:

        print('"' + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] + '"' + ", " + ligne[4][2:10] )


def affiche_longeur_18(text):
    for ligne in text:
        if re.search(r"275",ligne[0]):
          print('"' + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] + '"' + ", " + ligne[5]
              +" "+ ligne[6]+" "+ ligne[7])
        else:
            print( ligne[1]+ ", " + '"' + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]  + " " + ligne[4] +
                    " " + ligne[5]  + " " + ligne[6]+" " + ligne[7][:-1]+'"')


def affiche_longeur_19(text):
    for ligne in text:
          print('"' + ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]   +" "+ ligne[5]
                +" "+" "+ ligne[6]+" "+ ligne[7]+ '"'+ ", " + " " + ligne[9] + " " + ligne[10]  +" " + ligne[11]+" " + ligne[12])





def affiche100_len_1(len1):
    """ Cette fonction affiche les ligne qui ont um seul mot et ne commanssant pas par un nombre"""
    print("Ingrédients: " + len1[0] + ", " + "Quantité:     ")


def affiche100_len_2(len2):
    """ Cette fonction affiche les ligne qui ont deux mots et ne commanssant pas par un nombre"""
    if re.search(r"Feuilles", len2[0]+" "+len2[1]):
        print("Ingrédients: " + (len2[1]).replace("d'", "") + "  " + "Quantité: " + len2[0])
    else:
        print("Ingrédients: " + (len2[0]).replace("des", "") + " " + len2[1] + ", " + "Quantité:     ")

def affiche100_len_3(len3):
    """ Cette fonction affiche les ligne qui ont trois mots et ne commanssant pas par un nombre"""
    if re.search("Préparation|Finition", len3[0] + " " + len3[1] + " " + len3[2]):
        print(len3[0] + " " + len3[1] + " " + len3[2] + " Ingrédients: " + ",  " + "Quantité:     ")
    elif re.search(r"pour|du",len3[0] + " " + len3[1] + " " + len3[2]):
        print(len3[0] + " " + len3[1] + " " + len3[2] + " Ingrédients: " + len3[0] + ", " + "Quantité:     ")
    elif re.search(r"goût", len3[0] + " " + len3[1] + " " + len3[2]):
        print(len3[0] + " " + len3[1] + " " + len3[2] + " Ingrédients: " + len3[0] + ", " + "Quantité: " + len3[
            1] + " " + len3[2])
    elif re.search("quelques" , len3[0] + " " + len3[1] + " " + len3[2]):
        print(len3[0] + " " + len3[1] + " " + len3[2] + " Ingrédients: " + len3[2] + ", " + "Quantité: " + len3[
            0] + " " + len3[1])
    elif re.search("Quelques" ,len3[0] + " " + len3[1] + " " + len3[2]):
        print(len3[0] + " " + len3[1] + " " + len3[2] + " Ingrédients: " + len3[1] + ", " + "Quantité: " + len3[0])
    elif re.search("Zeste",len3[0] + " " + len3[1] + " " + len3[2]):
        print(len3[0] + " " + len3[1] + " " + len3[2] + " Ingrédients: " + len3[2] + ", " + "Quantité: " + (
        len3[1]).replace("d'", ""))
    else:
        print(len3[0] + " " + len3[1] + " " + len3[2] + " Ingrédients: " + len3[0] + " " + len3[1] + " " + len3[
            2] + ", " + "Quantité:     ")


def affiche100_len_4(len4):
    """ Cette fonction affiche les ligne qui ont um seul mot et ne commanssant pas par un nombre"""
    if re.search("Quelques",len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3]):
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] +
              " Ingrédients: " + len4[3] + ", " + "Quantité: " + len4[0] + " " + len4[1])
    elif re.search("Préparation" ,len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3]):
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] + " Ingrédients: " + ",  " + "Quantité:     ")
    elif re.search("pincée",len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3]):
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] + " Ingrédients: " + len4[
            3] + ",  " + "Quantité: " + len4[0] + " " + len4[1])
    elif re.search("sel",len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3]):
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] + " Ingrédients: " + len4[1] + " " + len4[
            3] + ",  " + "Quantité: ")
    elif re.search("citron",len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3]):
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] + " Ingrédients: " + len4[
            3] + ",  " + "Quantité: " + (len4[2]).replace("d'", ""))
    elif re.search("demi-lime" ,len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3]):
        chaine_lime = (len4[2] + ' ' + len4[3]).split("-")
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] + " Ingrédients: " + chaine_lime[
            1] + ",  " + "Quantité: " + (chaine_lime[0]).replace("d’", ""))
    elif re.search("quinzaine",len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3]):
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] + " Ingrédients: " + (len4[2]).replace("d’", "") + ",  " + "Quantité: " +
              len4[0] + " " + len4[1])

    else:
        print(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] +
              " Ingrédients: " + len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] + ", " + "Quantité:     ")

def affiche100_len_5(len5):
    """ Cette fonction affiche les ligne qui ont 5 mots et ne commanssant pas par un nombre"""
    if re.search("Préparation",len5[0] + " " + len5[1] + " " + len5[2] + " " + len5[3] + " " + len5[4]):
        print(len5[0] + " " + len5[1] + " " + len5[2] + " " + len5[3] + " " + len5[
            4] + " Ingrédients: " + ",  " + "Quantité:     ")
    elif re.search("Feuille" ,len5[0] + " " + len5[1] + " " + len5[2] + " " + len5[3] + " " + len5[4]):
        print(len5[0] + " " + len5[1] + " " + len5[2] + " " + len5[3] + " " + len5[4] + " Ingrédients: " + len5[
            2] + ",  " +
              "Quantité: " + len5[0] + " " + len5[3] + " " + len5[4])
    else:
        print(len5[0] + " " + len5[1] + " " + len5[2] + " " + len5[3] + " " + len5[4] + " Ingrédients: " +
              len5[0] + " " + len5[1] + " " + len5[2] + ",  " +
              "Quantité: " + len5[3] + " " + len5[4])

def affiche100_len_6(len6):

    if re.search("une",len6[0] + " " + len6[1] + " " + len6[2] + " " + len6[3] + " " + len6[4] + " " + len6[5]):
        print(  " Ingrédients: " +
              len6[0] + " " + len6[1] + " " + len6[2] + ",  " +  "Quantité: " + len6[4] + " " + len6[5])
    else:
        print( " Ingrédients: " + ",  " +  "Quantité: " )

def affiche100_len_7(len7):
    my_string = len7[0] + " " + len7[1] + " " + len7[2] + " " + len7[3] + " " + len7[4] + " " + len7[5]+ " " + len7[6]

    if re.search(r"moulin" , len7[0] + " " + len7[1] + " " + len7[2] + " " + len7[3] + " " + len7[4] + " " + len7[5]+ " " + len7[6]):
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

    #print(classer_text("ingredients.txt")[100])
    Val=classer_text("ingredients.txt")[8]
    #print(len(Val))
    #n=0
    for i in Val:
        #n +=1
        #if len(i)==7:
        print (i)
    #print(n)


    affiche_longeur3("ingredients.txt", 3)
    #affiche_longeur3(Val)
    #affiche_longeur100("ingredients.txt")
    # affiche100_len_6(['une', 'petite', 'tasse', 'de', 'riz', 'rond'])

    #affiche100_len_7(['trait', 'jus', 'de', 'citron', 'ou', 'de', 'lime'])
    #affiche_longeur_2(Val)
    #affiche_longeur_4(Val)
       #affiche_longeur_3(Val)
    #affiche_longeur_5(Val)
    #affiche_longeur_6(Val)
    #affiche_longeur_7(Val)
    #affiche_longeur_8(Val)
    #affiche_longeur_9(Val)
    #affiche_longeur_10(Val)
    #affiche_longeur_11(Val)
    #affiche_longeur_12(Val)
    #affiche_longeur_14(Val)
    #affiche_longeur_16(Val)
    #affiche_longeur_18(Val)
    #affiche_longeur_19(Val)



