class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        l1 = []
        for i in range(len(text1)+1):
            l2=[]
            for j in range(len(text2)+1):
                l2.append(0)
            l1.append(l2)
        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                if(i==0 or j==0):
                    continue
                if(text1[i-1] == text2[j-1]):
                    l1[i][j] = 1 + l1[i-1][j-1]
                else:
                    l1[i][j] = max(l1[i-1][j], l1[i][j-1])
        return(l1[len(text1)][len(text2)])
        