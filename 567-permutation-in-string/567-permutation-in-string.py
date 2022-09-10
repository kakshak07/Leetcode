from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        d1 = Counter(s1)
        for i in range(0, len(s2)-len(s1)+1):  
            sub = s2[i:i+len(s1)]
            d2 = Counter(sub)
            if d1 == d2:
                return True
        return False