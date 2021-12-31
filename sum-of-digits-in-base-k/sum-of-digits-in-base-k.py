class Solution:
    def sumBase(self, n: int, k: int) -> int:
        # w=[]
        su=0
        while(n>0):
            su = su + n%k
            n = n//k
        return(su)
            
        