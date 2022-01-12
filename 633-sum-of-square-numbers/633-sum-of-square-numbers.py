class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        a=0
        b=int(c**0.5)
        
        while(a<=b):
            w=a**2+b**2
            if(w==c):
                return(True)
            if(w>c):
                b=b-1
            else:
                a=a+1
        return(False)
        
        
