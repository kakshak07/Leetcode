class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        i = 1
        count = 1
        sumi = 1
        if n == 1:
            return 1
        while sumi<=n:
            i = i + 1
            sumi += i
            count = count + 1
        return count - 1