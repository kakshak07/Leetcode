class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        w=[]
        
        for i in range(numRows):
            t=[]
            if(i==0):
                t=[1]
                w.append(t)
                continue
            e=[0]+w[i-1]+[0]
            for j in range(len(e)-1):
                t.append(e[j]+e[j+1])
            w.append(t)
        return(w)
                
        