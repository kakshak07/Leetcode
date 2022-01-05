class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ini0=0
        fin0=0
        ini1=0
        fin1=0
        
        for i in s:
            if(i=="0"):
                ini0=ini0+1
                ini1=0
            if(i=="1"):
                ini1=ini1+1
                ini0=0
            fin0=max(fin0,ini0)
            fin1=max(fin1,ini1)
        if(fin0<fin1):
            return(True)
        return(False)
            
        