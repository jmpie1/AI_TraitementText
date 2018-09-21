import re
def get_engredient(text):
    """ mmMy fonction """
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
        #m = re.match(r"(\w+) (\w+) (\w+) (\w+)", text)
        #print(m.group(0))
        pass

    #print(re.match(r"(\w+) (\w+) (\w+)", text))
# get_engredient("2 cuillères à café de poudre à pâte")

get_engredient("6 poivre ")


