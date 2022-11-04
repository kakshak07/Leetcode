class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resultString = ""
        resultLength = 0
        
        for i in range(len(s)):
            leftP, rightP =i, i
            while leftP>=0 and rightP<len(s) and s[leftP] == s[rightP]:
                if resultLength < (rightP - leftP + 1):
                    resultString = s[leftP:rightP+1]
                    resultLength = rightP - leftP + 1
                leftP -= 1
                rightP += 1
            
            leftP, rightP =i, i+1
            while leftP>=0 and rightP<len(s) and s[leftP] == s[rightP]:
                if resultLength < (rightP - leftP + 1):
                    resultString = s[leftP:rightP+1]
                    resultLength = rightP - leftP + 1
                leftP -= 1
                rightP += 1
        return resultString