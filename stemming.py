class Stemming():
    def __init__(self, mot):

        self.mot = mot
        self.end_words = [
            ["eur", "euse","ais","ait","ons","ez","ont","ions","iez","îmes", "îtes", "is","it","ut","ûmes","ûtes","âmes",'âtes','ent',"as", "ssaient","ai","s","ement","x",""],
            ["iteur", "itrice","ateur","atrice","ation", "er"],
            ["aux", "al"],
            ["eaux", "eau"]
        ]
        self.results = []
        self.min = ""

    def cut(self):

        for i in self.end_words:
            if len(i) > 2:
                endword = len(i) - 1

                for j in range(endword):
                    len_word = len(i[j])

                    if i[j] == self.mot[-len_word:]:
                        self.results.append(self.mot[:-len_word] + i[-1])
                        print(self.mot + " => " + self.mot[:-len_word] + i[-1])
                
                try:  
                    self.min = self.results[0]
                    for i in self.results:
                        if len(i) < len(self.min):
                            self.min = i         
                            
                except:
                    continue      

            else:
                len_word = len(i[0])
                if i[0] == self.mot[-len_word:]:
                    self.min = self.mot + " => " + self.mot[:-len_word] + i[-1]
                    
        return self.min
                

test1 = Stemming("hibou")
print(test1.cut())