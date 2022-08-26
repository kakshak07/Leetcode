class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        dick = {}
        
        for i in nums:
            dick[i]=1
        cout = 1
        while(cout in dick):
            cout+=1
        return(cout)
        