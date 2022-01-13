class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans=0
        l=r=0
        m={}
        for letter in s:
            if letter in m.keys():
                l=max(l,m[letter]+1)
            ans=max(ans,r-l+1)
            m[letter]=r
            r+=1
        return ans
        