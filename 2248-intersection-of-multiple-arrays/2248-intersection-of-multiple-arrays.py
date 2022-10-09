class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        t = nums[0]
        w = []
        if len(nums) == 1:
            return(sorted(nums[0]))
        for i in t:
            xy = 0
            for j in range(1, len(nums)):
                if i not in nums[j]:
                    break
                if j==len(nums)-1:
                    xy = 1
            if xy == 1:
                w.append(i)
        return(sorted(w))
                    
                    
                    
        