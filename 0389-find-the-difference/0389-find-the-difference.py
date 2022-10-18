class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import defaultdict
        maphash = defaultdict(int)
        
        for i in s:
            maphash[i] += 1
        for j in t:
            maphash[j] -= 1
        for t in maphash:
            if maphash[t]!=0:
                return t
        