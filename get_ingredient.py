import re
from typing import Any


def affiche_longeur_3(text):
    """
    Permet d'afficher les textes commancant par un chiffre et dont le nombre de trois est mots
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


affiche_longeur_3("2 gousses d'ail")
