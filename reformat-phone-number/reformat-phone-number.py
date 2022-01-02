class Solution:
    def reformatNumber(self, number: str) -> str:
        s=number.replace("-","").replace(" ","")
        i=0
        t=len(s)
        w=t//3
        r=t%3
        if(r==0):
            re=""
            for i in range(len(s)):
                re=re+s[i]
                if(i==len(s)-1):
                    break
                if((i+1)%3==0):
                    re=re+"-"
            return(re)
        if(r==2):
            re=""
            for i in range(len(s)-2):
                re=re+s[i]
                if(i==len(s)-1):
                    break
                if((i+1)%3==0):
                    re=re+"-"
            re=re+s[len(s)-2:len(s)]
            return(re)
        if(r==1):
            q=s[len(s)-4:len(s)]
            re=""
            for i in range(len(s)-4):
                re=re+s[i]
                if(i==len(s)-1):
                    break
                if((i+1)%3==0):
                    re=re+"-"
            re=re+q[:2]
            re=re+"-"
            re=re+q[2:4]
            return(re)
            
                
                