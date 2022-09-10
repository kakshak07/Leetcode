from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        d1 = Counter(s1)
        for i in range(len(s2)):  
            sub = s2[i:i+len(s1)]
            d2 = Counter(sub)
            if d1 == d2:
                return True
        return False