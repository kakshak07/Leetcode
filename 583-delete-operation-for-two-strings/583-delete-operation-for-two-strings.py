class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        l1 = []
        
        for i in range(len(word1)+1):
            l2 = []
            for j in range(len(word2)+1):
                l2.append(0)
            l1.append(l2)
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if(i==0 or j==0):
                    continue
                if(word1[i-1]==word2[j-1]):
                    l1[i][j] = 1 + l1[i-1][j-1]
                else:
                    l1[i][j] = max(l1[i-1][j], l1[i][j-1])
        return(len(word1)+len(word2) - 2*l1[len(word1)][len(word2)])
            