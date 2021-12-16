class Stemming():
    def __init__(self, mot):
        
        self.mot = mot
        self.end_words = ["eur","euse"]

    def test(self):

        for i in self.end_words:
            if i in self.mot:
                print(self.mot)
            else:
                print("ça marche pas")
                

test1 = Stemming("chanteur")
print(test1.test())
