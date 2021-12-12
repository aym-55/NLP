import re
import json

class Tokenize():
    def __init__(self, text):
        self.text = text
        self.all_words = []
        self.all_sentences = []
        self.matrix = []
        
        stopwords = open('stop_words.json', 'r')
        self.stopwords = json.load(stopwords)     

    def text_to_words(self):

        self.sentences = re.split("[.?!:;]", self.text)

        for sentence in self.sentences:
            self.sentence_in_words = re.split("[ '\n,-]", sentence)
            self.sentence_in_words = [x.lower() for x in self.sentence_in_words]
            self.del_useful_words(self.sentence_in_words)
            
            if self.sentence_in_words != []:
                self.all_sentences.append(self.sentence_in_words)

    def del_useful_words(self, liste):
        for word in reversed(liste):
            if word in self.stopwords or word.lower() in self.stopwords:
                liste.remove(word)

    def tokenize(self):
        
        self.all_words = list(set(sum(self.all_sentences, [])))
        self.all_words.sort()              
                
        for sentence in self.all_sentences:
            new_occur = []
            
            for word in self.all_words:
                nb_occur = sentence.count(word)
                new_occur.append(nb_occur)
            
            self.matrix.append(new_occur)
            
    def affiche(self):

        self.text_to_words()
        self.tokenize()

        result = "{}  [{}]\n------------------------------------------------------------------------------------------\n{}  [{}]\n".format(self.all_sentences, 
                                                                                                    len(self.all_sentences), self.all_words, len(self.all_words))
        for new_occur in self.matrix:
            result += "{}  [{}]\n".format(new_occur, sum(new_occur))
        return result
                        


texte = ("""En mon cœur n'est point escrite
         La rose ny autre fleur,
         C'est toy, blanche Marguerite,
         Par qui j'ay cette couleur.
         N'es-tu celle dont les yeux
         Ont surpris
         Par un regard gracieux
         Mes esprits ?
         Puis que ta sœur de haut pris,
         Ta sœur, pucelle d'élite,
         N'est cause de ma douleur,
         C'est donc par toy, Marguerite
         Que j'ay pris ceste couleur.
         Ma couleur palle nasquit,
         Quand mon cœur
         Pour maistresse te requit ;
         Mais rigueur
         D'une amoureuse langueur
         Soudain paya mon mérite,
         Me donnant ceste pâleur
         Pour t'aimer trop, Marguerite,
         Et ta vermeille couleur.
         Quel charme pourroit casser
         Mon ennuy
         Et ma couleur effacer
         Avec luy ?
         De l'amour que tant je suy
         La jouissance subite
         Seule osteroit le malheur
         Que me donna Marguerite,
         Par qui j'ay cette couleur.""")
            
test1 = Tokenize(texte)
test2 = Tokenize("Bonjour Bonjour. Ceci est un est test ! est ce que ça va marcher ? on verra : tabernak! bonjour") 
test3 = Tokenize("Voyons si cela marche ! mais bien sûr ça va marcher, n'est-ce pas ? etrange.") 

print("================================================= TEST 1 ==================================================================================")
print(test1.affiche())
print("================================================= TEST 2 ==================================================================================")
print(test2.affiche())
print("================================================= TEST 3 ==================================================================================")
print(test3.affiche())
print("===========================================================================================================================================")