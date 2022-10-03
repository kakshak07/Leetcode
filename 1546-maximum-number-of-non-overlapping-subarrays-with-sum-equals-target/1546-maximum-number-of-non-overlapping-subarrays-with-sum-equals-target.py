class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        f = {}
        s = 0
        count = 0
        f[0] = 1
        for i in nums:
            s += i
            if s-target in f:
                count += 1
                f = {}
            f[s] = 1
        return(count)
            
            