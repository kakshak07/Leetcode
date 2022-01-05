class Solution:
    def maxPower(self, s: str) -> int:
        
        t=0
        ma=0
        chr=s[0]
        
        for i in s:
            if(i==chr):
                t=t+1
            else:
                ma=max(ma,t)
                chr=i
                t=1
        return(max(ma,t))
        