import re
def get_engredient(text):
    """ Trouver les ingredients ainsi que leur quantité"""
    if(text[0].isnumeric()):
         splitText=text.split()
         if(len(splitText)== 3 ):
             if(re.match(r"(\w+) (\w+) (\w+)", text)==None):
                  #m1 = re.match(r"(\w+) (\w+) (\w+)", text)
                  print(splitText[0] + ' ' + splitText[1] + ', ' + splitText[2])
             else:
                 print(splitText[0]+' '+splitText[1]+', '+splitText[2])
         if (len(splitText) == 2):
             print(splitText[0]+', '+splitText[1])
    else:

        pass

    #print(re.match(r"(\w+) (\w+) (\w+)", text))
# get_engredient("2 cuillères à café de poudre à pâte")

get_engredient("6 poivre ")


