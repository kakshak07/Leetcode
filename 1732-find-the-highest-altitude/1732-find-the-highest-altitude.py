class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        t=[]
        
        t.append(0)
        ma=gain[0]
        
        for i in range(len(gain)):
            q=t[len(t)-1]
            w=q+gain[i]
            t.append(w)
            ma=max(ma,w)
        if(ma<0):
            return(0)
        return(ma)
        