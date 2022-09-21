class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        abcd = tops + bottoms
        
        d = {}
        
        for i in abcd:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        t=None
        w=None
        for i in d:
            if(t==None):
                t=i
                w=d[i]
            else:
                if(d[i]>w):
                    t=i
                    w=d[i]
        tops_dice = 0
        bottom_dice = 0
        for i in range(len(tops)):
            if(tops[i]==t):
                continue
            elif(tops[i]!=t and bottoms[i]==t):
                tops_dice+=1
            else:
                return(-1)
            
        for i in range(len(bottoms)):
            if(bottoms[i]==t):
                continue
            elif(bottoms[i]!=t and tops[i]==t):
                bottom_dice+=1
            else:
                return(-1)
        return(min(bottom_dice,tops_dice))
                    
        