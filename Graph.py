from matplotlib import pyplot as plt
from collections import Counter

def nb_mot_par_ligne(file, val=100):
    """ Calcul de la liste qui contient le nombre de mots des chaque ligne
        La valeur par defaut étant celle qui calcule la longeur des lignes ne
        commancant pas par nombre"""
    with open(file, encoding='utf8') as fichier:
        if val !=100:
            return  sorted([len(w.split()) for w in fichier if w[0].isnumeric()])
        else:

            return sorted([len(w.split()) for w in fichier if not w[0].isnumeric()])[2:]
print(nb_mot_par_ligne("ingredients.txt", 6))
print(Counter(nb_mot_par_ligne("ingredients.txt",1)))
#plt.hist(nb_mot_par_ligne("ingredients.txt", 6))
#plt.show()


data = Counter(nb_mot_par_ligne("ingredients.txt",1))
names = list(data.keys())
print(names)
values = list(data.values())
print(values)

#tick_label does the some work as plt.xticks()
plt.bar(range(len(data)),values,tick_label=names)
plt.savefig('bar.png')
plt.xlabel('Nombre de mot par ligne', fontweight='bold', color = 'orange', fontsize='17', horizontalalignment='center')
plt.ylabel('Nombre de ligne', fontweight='bold', color = 'orange', fontsize='17', horizontalalignment='center')

plt.show()