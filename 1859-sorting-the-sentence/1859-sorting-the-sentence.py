class Solution:
    def sortSentence(self, s: str) -> str:
        
        abcd = s.split(" ")
        a=[]
        for i in range(len(abcd)):
            a.append(abcd[i][-1])
            abcd[i] = abcd[i][:-1]
        w=[]
        for i in range(1,len(abcd)+1):
            w.append(abcd[a.index(str(i) ) ])
            
        return(" ".join(w))
        