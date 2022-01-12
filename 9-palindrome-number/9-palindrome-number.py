class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        w=str(x)
        
        def palin(x,i):
            if(i>len(w)//2):
                return(True)
            return((x[i]==x[len(x)-1-i]) and palin(x,i+1))
        i=0
        return(palin(w,i))
        