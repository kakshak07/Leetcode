class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ini1=0
        fin1=0
        
        for i in nums:
            if(i==1):
                ini1=ini1+1
                print(ini1)
            else:
                fin1=max(fin1,ini1)
                ini1=0
            
        return(max(fin1,ini1))
        