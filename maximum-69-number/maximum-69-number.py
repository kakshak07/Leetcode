class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)
        w=""
        q=0
        for i in range(len(num)):
            if(num[i]=="6"):
                w=num[0:i]
                w=w+"9"
                w=w+num[i+1:len(num)]
                # num[i]="9"
                q=1
                break
        if(q==0):
            return(num)
        return(w)
        