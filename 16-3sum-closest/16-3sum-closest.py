class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = None
        sum_min_diff = None
        
        nums.sort()
        for i in range(len(nums)):
            tot = nums[i]
            a = i+1
            b = len(nums)-1
            
            while(a<b):
                new_s = tot+nums[a]+nums[b]
                if(min_diff==None):
                    min_diff = new_s
                    sum_min_diff = abs(new_s-target)
                else:
                    if(abs(target-new_s)<sum_min_diff):
                        min_diff = new_s
                        sum_min_diff = abs(new_s-target)
                if(new_s<target):
                    a=a+1
                else:
                    b=b-1
                
        return(min_diff)
                    
                
                        
                        
        