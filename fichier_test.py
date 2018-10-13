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


def affiche_longeur_3(text):
    """
    Permet d'afficher les textes commancant par un chiffre et dont le nombre de mot est trois
    :type text: string
    :type nb: nombre d'élément dans la liste
    """
    # dico={}
    # dico = classer_text(text)
    #
    # dico =dico[nb]
    # m = 0
    for split_text in text:
      # m += 1
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
        print(' "{1}", "{0}"'.format(ligne[0],(ligne[1]).replace("d'","")))

def affiche_longeur_4(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " +ligne[3]

        if re.search(r"purée$|échalote[s]?|oignon", my_string) :
            if re.search("française,", my_string):
                print(' "{0}", "{1}"'.format(ligne[1] + " " + (ligne[2]).replace(",","") , ligne[0]))
            elif re.search(r"échalote", my_string):
                if re.search(r"tasse",my_string):
                    print(' "{0}", "{1}" '.format(ligne[2], ligne[0]+" "+ligne[1]))
                else:
                  print(' "{0}", "{1}" '.format(ligne[1], ligne[0]))
            else:
                print(' "{0}", "{1}" '.format(ligne[1], ligne[0] ))
        elif re.search(r"(\d|½) ((\w+)|(c.à.c)|(c.à.s)) de (\w+)", my_string):
            if ("lime" in ligne):
                print(' "{0}", "{1}" '.format(ligne[1]+" "+ ligne[2] + " "+ ligne[3] ,ligne[0] ))
            else:
                print(' "{0}", "{1}" '.format(ligne[3] , ligne[0] + " " +ligne[1]))
        elif re.search(r"hachée$|d’ail,|saucisses", my_string):
            print(' "{0}", "{1}" '.format(ligne[1] + " " +(ligne[2].replace(",","")).replace("d’",""), ligne[0] ))
        # elif re.search(r"", my_string):

        else:
            print(' "{0}", "{1}" '.format(ligne[2].replace("d'","").replace("d’","") + " " +ligne[3],ligne[0] + " " +ligne[1]))


def affiche_longeur_5(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]
        if re.search(r"\d (\w+) de (\w+) (\w+)", my_string):
               if "noix" == ligne[1]:
                   print(' "{0}", "{1}" '.format(ligne[3],ligne[0] + " " + ligne[1]))
               else:
                   print(' "{0}", "{1}" '.format(ligne[3] + " " + ligne[4], ligne[0] + " "+ligne[1]))
        elif  re.search(r"café|(c. à .s)",my_string):
            print(' "{0}", "{1}" '.format(ligne[0] + " " + ligne[1]+ " "+ligne[3],ligne[4].replace("d’","")))
        elif re.search(r"sauce",my_string):
            print(' "{0}", "{1}" '.format(ligne[3] + " " + ligne[4] ,ligne[0] + " " + ligne[1]))
        elif "cheddar" == ligne[3]:
            print(' "{0}", "{1}" '.format(ligne[2] + " " + ligne[3] ,ligne[0]+ " " +ligne[1]  ))
        elif re.search(r"\d petit oignon",my_string):
            print(' "{0}", "{1}" '.format(ligne[1] + " " + ligne[2] + " " + ligne[3],ligne[0]))
        elif "farine" == ligne[4]:
            print(' "{0}", "{1}" '.format(ligne[0] + " " + ligne[1] + " " + ligne[2],ligne[4]))
        elif re.search(r"Kg$",my_string):
            print(' "{0}", "{1}" '.format( ligne[1],ligne[0]+ " (" + ligne[3]+ligne[4]+ ")"))
        else:
            print(' "{0}", "{1}" '.format( ligne[2].replace("d’","") + " "+ligne[3] + " " + ligne[4],ligne[0] + " "+ligne[1]))


def affiche_longeur_6(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]
        if re.search(r"\d (c.) (à) (\w+) de (\w+)", my_string) or "bicarbonate" in ligne:
            print(' "{1}", "{0}" '.format(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3], ligne[5]))
        elif  re.search(r"(\d+|\d) (\w+) (de) (\w+) (\w+) (\w+)", my_string):
            if "congre" in ligne:
                print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[ 1] + " ("+ligne[ 4]+ ligne[ 5]+ ")", ligne[3]))
            else:
                print(' "{1}", "{0}" '.format(ligne[0]  +" " + ligne[1], ligne[3] + " " + ligne[4] +" " +ligne[5]))
        elif re.search(r"(\()", my_string):
            print(' "{0}", "{1}" '.format((ligne[4]).replace("d’","")  +" " + ligne[5],ligne[0] + " " + ligne[ 1] + " "+ligne[ 2]+ " "+ligne[ 3]))

        elif re.search(r"(c.à.s)", my_string):
            print(' "{1}", "{0}" '.format(ligne[0] + " " + ligne[1],ligne[3] + " " + ligne[4]+" " + ligne[5]))

        elif re.search(r"décorer$", my_string):
            print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1],(ligne[3]).replace(",","") ))
        elif re.search(r"pommes", my_string):
            print(' "{1}", "{0}" '.format(ligne[0],ligne[1] + " " + ligne[2] ))

        elif re.search(r"pièce", my_string):
            print(' "{0}", "{1}" '.format(ligne[3], ligne[0] + " " + ligne[1]
                  + " " +"("+ligne[4].replace("d'","")+" "+ligne[5]+")" ))


        elif re.search(r"d'olive$", my_string):
            print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3],ligne[4] + " " + ligne[5]))

        elif re.search(r"sucre$", my_string):
            print(' "{1}", "{0}" '.format(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3],ligne[5] ))
        else:
            print(' "{1}", "{0}" '.format(ligne[0] + " " + ligne[1] + " " + ligne[2] , ligne[3]+" "+ ligne[4]+" " + ligne[5]))

def affiche_longeur_7(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " + ligne[6]

        if re.search( r"((ml\))|(g\))|(soupe\)))",ligne[5]):
            print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1] + " " + ligne[2] + " " +
                  ligne[3] + " "+ ligne[4] + " " + ligne[5],ligne[6].replace("d’","")))
        elif re.search( r"(claire$|foncée$|frisé$|Paris$|verts$)",ligne[6]):
            print(' "{0}", "{1}" '.format(ligne[3] + " " + ligne[4] + " " + ligne[5] + " " +
                  ligne[6],ligne[0] + " " + ligne[1]))

        elif re.search( r"(blanc$|fraîche$|râpé$|moulue$|César$|séché$|balsamique$|pla$)",ligne[6]):
            if "rhum"== ligne[5] or "nam"== ligne[5]:
                print(' "{0}", "{1}" '.format(ligne[5] + " " +
                      ligne[6],ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]))
            else:
                print(' "{0}", "{1}" '.format( ligne[5] + " " +
                  ligne[6],ligne[0] + " " + ligne[1]+ " " + ligne[2] + " " + ligne[3]))
        elif re.search( r"(purée$)",ligne[6]):
            print(' "{0}", "{1}" '.format(ligne[2] + " " + ligne[3] + " " +
                  ligne[4] ,ligne[0] + " " + ligne[1] ))
        elif re.search( r"(rawit)",ligne[6]):
            print(' "{0}", "{1}" '.format( ligne[1] + " " + ligne[2] + " " +ligne[3]+ " " + ligne[4]+
                  " " +ligne[5] + " " + ligne[6], ligne[0] ))
        elif re.search( r"rincées$",ligne[6]):
            print(' "{0}", "{1}" '.format( ligne[1] + " " + ligne[2],ligne[0] ))

        elif re.search( r"g$",ligne[6]):
            print(' "{0}", "{1}" '.format(ligne[3],ligne[0]+" " +ligne[1] + " (" + ligne[5] + " " +ligne[6]+")" ))
        else:
            print(' "{0}", "{1}" '.format( (ligne[4]).replace("d’","") + " " + ligne[5] + " " + ligne[6], ligne[0]+  " "+ligne[1] + " " + ligne[2]+ " " + ligne[3]))

def affiche_longeur_8(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]
        if re.search(r"râpé$", ligne[7]):
            print(' "{0}", "{1}" '.format( ligne[6] , ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4] + " " + ligne[5]))
        elif re.search(r"(goût$)", ligne[7]):
            print(' "{0}", "{1}" '.format( ligne[4], ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[5] + " " + ligne[6]+" " + ligne[7]))
        elif re.search(r"(blanc$|soya$|d’olive$)", ligne[7]):
            print(' "{0}", "{1}" '.format( ligne[6].replace("d’","")+" " + ligne[7],ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4] + " "+ligne[5] ))
        elif re.search(r"(safran$)", ligne[7]):
            print(' "{0}", "{1}" '.format( ligne[7] ,ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4] + " "+ligne[5] ))
        elif re.search(r"(deux$)", ligne[7]):
            print(' "{0}", "{1}" '.format( ligne[2][2:5].replace("d’",""), ligne[0] + " " + ligne[1] ))
        elif re.search(r"(d'érable$)", ligne[7]):
            print(' "{0}", "{1}" '.format( ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7],ligne[0] + " " + ligne[1] ))

        else:
            print(' "{0}", "{1}" '.format(ligne[5] + " " + ligne[6] + " " + ligne[7],ligne[0]+  " "+ligne[1] + " " + ligne[2]+ " " + ligne[3] ))


def affiche_longeur_9(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]+" " + ligne[8]
        if re.search(r"(biseaux$)",ligne[8]):
            print(' "{0}", "{1}" '.format(ligne[4] + " " + ligne[5],ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]) )

        elif re.search(r"(arachide$)",ligne[8]):
            print(' "{0}", "{1}" '.format( ligne[4].replace("d’", "") + " " + ligne[5]+" "+ ligne[6]+" " + ligne[7]+" " + ligne[8], ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]) )

        elif re.search(r"(nettoyées$)",ligne[8]):
            print(' "{0}", "{1}" '.format( ligne[5].replace(",", ""),ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]) )
        elif re.search(r"(l’eau$)",ligne[8]):
            print(' "{0}", "{1}" '.format(ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]+" " + ligne[8], ligne[0] + " " + ligne[1] ))
        elif re.search(r"(dorées$)",ligne[8]):
            print(' "{0}", "{1}" '.format( ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]+" " + ligne[8],ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]))

        else:
            print(' "{0}", "{1}" '.format(ligne[6] + " " + ligne[7] + " " + ligne[8],
                                          ligne[0]+  " "+ligne[1] + " " + ligne[2]+ " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]))



def affiche_longeur_10(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]+" " + ligne[8]+" " + ligne[9]
        if re.search(r"(égoutté[e]?s$)",my_string):
            print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3],ligne[5]+ " " +\
                    ligne[6]+"" +(ligne[7] + " " + ligne[8]).replace("rincés et","")))
        elif re.search(r"(râpé$)",my_string):
            print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]
                  +  " " + ligne[4]+ " " + ligne[5], ligne[7]))
        elif re.search(r"(beurre,)",my_string):
            print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]
                  +  " " + ligne[4]+ " " + ligne[5]+" " + ligne[9], ligne[7]))

        elif re.search(r"(secs)", my_string):
            print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1], ligne[3] +" "+ ligne[4] +" "+ ligne[5]))
        else:

            print(' "{1}", "{0}" '.format(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6].replace("de",""),ligne[7].replace("d’","")+" " + ligne[8]+ ", "))

def affiche_longeur_11(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]+" " + ligne[8]+" " + ligne[9]+" "+ligne[10]

        if re.search(r"(morceaux)",my_string):
            print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1], ligne[2] + " " + ligne[3]
                 + " " + ligne[4]))
        elif re.search(r"(blanc)",my_string):

            print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5], ligne[7] + " " + ligne[8]
                 + " " + ligne[9]+ " " + ligne[10]))

        elif re.search(r"(langoustines|tomates)",my_string):

            print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]
                 ,ligne[5] + " " + ligne[6]
                 + " " + (ligne[7].replace(",","")).replace("et","")))
        elif re.search(r"(pain)",my_string):

            print(
                ' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1] , ligne[3] + " " + ligne[4]))

        elif re.search(r"(coriandre)",my_string):

            print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]
                 , ligne[5] + " ou " + ligne[10]))

        elif re.search(r"(moulu)",my_string):

            print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]
                 + " " + ligne[5],ligne[7] + " ou " + ligne[8]))

        else:

            print(' "{1}", "{0}" '.format(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]
              , ligne[4].replace("d’","")+" " + ligne[5]))

def affiche_longeur_12(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]+" " + ligne[8]+" " + ligne[9]+" "+ligne[10]+" "+ligne[11]

        if re.search(r"(concassés$)",my_string):
            print(' "{0}", "{1}" '.format(ligne[7]+" " + ligne[8]+" " + ligne[9]+" "+ligne[10], ligne[0] + " " + ligne[1] + " "
                  + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]))
        else:
            print(' "{0}", "{1}" '.format(ligne[1] + " "+ ligne[2].replace(",",""), ligne[0] ))

def affiche_longeur_14(text):
    for ligne in text:
        my_string = ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]+ " " + ligne[4]+ " " + ligne[5]+ " " +\
                    ligne[6]+" " + ligne[7]+" " + ligne[8]+" " + ligne[9]+" "+ligne[10]+" "+ligne[11]+" "+ligne[12]\
                    +" " + ligne[13]
        print(' "{0}", "{1}" '.format(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] , ligne[4][2:]+ " " + ligne[5]))


def affiche_longeur_16(text):
    for ligne in text:
        print(' "{0}", "{1}" '.format(ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3] , ligne[4][2:10] ))


def affiche_longeur_18(text):
    for ligne in text:
        if re.search(r"275",ligne[0]):
            print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3], ligne[5]
              +" "+ ligne[6]+" "+ ligne[7]))
        else:
            print(' "{0}", "{1}" '.format(ligne[1], ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]  + " " + ligne[4] +
                    " " + ligne[5]  + " " + ligne[6]+" " + ligne[7][:-1]))


def affiche_longeur_19(text):
    for ligne in text:
        print(' "{1}", "{0}" '.format( ligne[0] + " " + ligne[1] + " " + ligne[2] + " " + ligne[3]   +" "+ ligne[5]
                +" "+" "+ ligne[6]+" "+ ligne[7], ligne[9] + " " + ligne[10]  +" " + ligne[11]+" " + ligne[12]))





def affiche100_len_1(len1):
    """ Cette fonction affiche les ligne qui ont um seul mot et ne commanssant pas par un nombre"""
    print(' "{0}", "{1}" '.format( len1[0] , "Quantité:     "))


def affiche100_len_2(len2):
    """ Cette fonction affiche les ligne qui ont deux mots et ne commanssant pas par un nombre"""
    if re.search(r"Feuilles", len2[0]+" "+len2[1]):
        print(' "{1}", "{0}" '.format( (len2[1]).replace("d'", ""), len2[0]))
    else:
        print(' "{0}", "{1}" '.format( (len2[0]).replace("des", "") + " " + len2[1], "Quantité:     "))

def affiche100_len_3(len3):
    """ Cette fonction affiche les ligne qui ont trois mots et ne commanssant pas par un nombre"""
    if re.search("Préparation|Finition", len3[0] + " " + len3[1] + " " + len3[2]):
        print(' "{0}", "{1}" '.format( " Ingrédients: " ,"Quantité:     "))
    elif re.search(r"pour|du",len3[0] + " " + len3[1] + " " + len3[2]):
        print(' "{0}", "{1}" '.format(  len3[0], "Quantité:     "))
    elif re.search(r"goût", len3[0] + " " + len3[1] + " " + len3[2]):
        print(' "{0}", "{1}" '.format( len3[0],  len3[
            1] + " " + len3[2]))
    elif re.search("quelques" , len3[0] + " " + len3[1] + " " + len3[2]):
        print(' "{0}", "{1}" '.format( len3[2], len3[
            0] + " " + len3[1]))
    elif re.search("Quelques" ,len3[0] + " " + len3[1] + " " + len3[2]):
        print(' "{0}", "{1}" '.format(len3[1], len3[0]))
    elif re.search("Zeste",len3[0] + " " + len3[1] + " " + len3[2]):
        print(' "{0}", "{1}" '.format( len3[2],(
        len3[1]).replace("d'", "")))
    else:
        print(' "{0}", "{1}" '.format(len3[0] + " " + len3[1] + " " + len3[
            2], "Quantité:     "))


def affiche100_len_4(len4):
    """ Cette fonction affiche les ligne qui ont um seul mot et ne commanssant pas par un nombre"""
    if re.search("Quelques",len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3]):
        print(' "{0}", "{1}" '.format(  len4[3] ,  len4[0] + " " + len4[1]))
    elif re.search("Préparation" ,len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3]):
        print(' "{0}", "{1}" '.format( " Ingrédients: "  , " Quantité: "))
    elif re.search("pincée",len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3]):
        print(' "{0}", "{1}" '.format( len4[
            3], len4[0] + " " + len4[1]))
    elif re.search("sel",len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3]):
        print(' "{0}", "{1}" '.format(len4[1] + " " + len4[
            3] , "Quantité: "))
    elif re.search("citron",len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3]):
        print(' "{0}", "{1}" '.format(len4[
            3], (len4[2]).replace("d'", "")))
    elif re.search("demi-lime" ,len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3]):
        chaine_lime = (len4[2] + ' ' + len4[3]).split("-")
        print(' "{0}", "{1}" '.format( chaine_lime[
            1] , (chaine_lime[0]).replace("d’", "")))
    elif re.search("quinzaine",len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3]):
        print(' "{0}", "{1}" '.format((len4[2]).replace("d’", "") ,
              len4[0] + " " + len4[1]))

    else:
        print(' "{0}", "{1}" '.format(len4[0] + " " + len4[1] + " " + len4[2] + " " + len4[3] , "Quantité:     "))

def affiche100_len_5(len5):
    """ Cette fonction affiche les ligne qui ont 5 mots et ne commanssant pas par un nombre"""
    if re.search("Préparation",len5[0] + " " + len5[1] + " " + len5[2] + " " + len5[3] + " " + len5[4]):
        print(' "{0}", "{1}" '.format(" Ingrédients: " , "Quantité:     "))
    elif re.search("Feuille" ,len5[0] + " " + len5[1] + " " + len5[2] + " " + len5[3] + " " + len5[4]):
        print(' "{0}", "{1}" '.format( len5[
            2] ,  len5[0] + " " + len5[3] + " " + len5[4]))
    else:
        print(' "{0}", "{1}" '.format(len5[0] + " " + len5[1] + " " + len5[2] ,len5[3] + " " + len5[4]))

def affiche100_len_6(len6):

    if re.search("une",len6[0] + " " + len6[1] + " " + len6[2] + " " + len6[3] + " " + len6[4] + " " + len6[5]):
        print(' "{0}", "{1}" '.format(len6[0] + " " + len6[1] + " " + len6[2], len6[4] + " " + len6[5]))
    else:
        print(' "{0}", "{1}" '.format(" Ingrédients: " ,  "Quantité:    " ))

def affiche100_len_7(len7):
    my_string = len7[0] + " " + len7[1] + " " + len7[2] + " " + len7[3] + " " + len7[4] + " " + len7[5]+ " " + len7[6]

    if re.search(r"moulin" , len7[0] + " " + len7[1] + " " + len7[2] + " " + len7[3] + " " + len7[4] + " " + len7[5]+ " " + len7[6]):
        print(' "{0}", "{1}" '.format(len7[0] + " " + len7[1] + " " + len7[2] + " " + len7[3] + " " + len7[4]
            , len7[5]+ " " + len7[6]))
    else:
        print(' "{0}", "{1}" '.format( len7[1] + " " + len7[2] + " " + len7[3] + " " + len7[4]+ " " +len7[5]+" "+len7[6]
              , len7[0]))
def affiche_longeur_100(ma_liste):
    """
    Cette fonction extraite des informations dans les ligne qui ne commencent pas par un nombre
    :param ma_liste: liste contenant des listes, chaque sous liste contient les lignes de même nombre de mots
    :return: None
    """
    for ligne in  ma_liste:
        lmot = len(ligne)
        eval("affiche100_len_"+str(lmot)+"("+str(ligne)+")")


def affiche_longeur_n(text, start_with_number=False, choice_len_start_with_number=0):
    """
    Cette fonction extrait les information dans les ligne commancant par un nombre
    :param text: fichier à lire
    :param start_with_number: boolean permet de selectionner les lignes commancant par un nombre ou non
    :param choice_len_start_with_number: numeric, si on choisit les lignes commancant par un nombre; on peut préciser
           si on veut afficher les informations de toutes les lignes  ou spécifier les ligne voulues (en fonction du nombre
           de mot par lignes).
    :return:
    """
    if choice_len_start_with_number not in [2,3,4,5,6,7,8,9,10,11,12,14,16,18,19]:
        print("Pour les ligne ne commencant pas par un nombre le nombre de mot par ligne est indiqué ci-dessous")
        print([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 19])
        print("Veullez changer la valeur de paramètre 'choice_len_start_with_number': Ex choice_len_start_with_number = 4")

        return
    ma_liste = classer_text(text)
    if start_with_number:
        if not choice_len_start_with_number:
          for i in ma_liste.keys():
            if i !=100:
              eval("affiche_longeur_"+str(i)+"("+str(ma_liste[i])+")")
        else:
            eval("affiche_longeur_" + str(choice_len_start_with_number) + "(" + str(ma_liste[choice_len_start_with_number]) + ")")
    else:
        affiche_longeur_100(ma_liste[100])


def affiche_tout(text):
    ma_liste = classer_text(text)
    for i in ma_liste.keys():
        eval("affiche_longeur_" + str(i) + "(" + str(ma_liste[i]) + ")")

if __name__ == "__main__":
    affiche_longeur_n("ingredients.txt")
    #affiche_longeur_n("ingredients.txt", True, 19)
    #affiche_tout("ingredients.txt")