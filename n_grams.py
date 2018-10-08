import nltk
#nltk.download('punkt')
#from nltk.tokenize import word_tokenize, sent_tokenize

with open('proverbes.txt', encoding='utf8') as fichier:
 for raw in fichier:


     tokens = nltk.word_tokenize(raw)
     #print(raw)
     #print(tokens)
     #print(" FIN")

    #Create your bigrams trigrams
     bgs = nltk.bigrams(tokens)

    
    #
    # #compute frequency distribution for all the bigrams in the text
     fdist = nltk.FreqDist(bgs)
     for k,v in fdist.items():
      if k ==('a', 'beau'):
           print("=========")
           print("Keys:             " + str(k), "Values "+ str(v))