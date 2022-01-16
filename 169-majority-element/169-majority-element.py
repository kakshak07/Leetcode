class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma=0
        
        t={}
        count=0
        for i in range(len(nums)):
            if(nums[i] in t):
                t[nums[i]]=t[nums[i]]+1
            else:
                t[nums[i]]=1
        print(t)
        for i in t:
            if(t[i]>len(nums)//2):
                count=i
        return(count)
            