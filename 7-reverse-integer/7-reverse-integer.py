class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1])
        
        if res >= 2**31 -1:
            return 0
        
        return res if x > -1 else res * -1