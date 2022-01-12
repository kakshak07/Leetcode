class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
        p=""
        
        for i in range(len(b)):
            p=p+str(b[i])
        return(pow(a,int(p),1337))
    
