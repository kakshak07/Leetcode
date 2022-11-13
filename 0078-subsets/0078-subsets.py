class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        list_of_nums = []
        
        res = []
        
        def dfs(i):
            if i>=len(nums):
                list_of_nums.append(res.copy())
                return
            res.append(nums[i])
            dfs(i+1)
            res.pop()
            dfs(i+1)
            
            # res.append()
        dfs(0)
        return list_of_nums