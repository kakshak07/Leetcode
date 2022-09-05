class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        
        
        while(len(str(num))!=1):
            abcd = 0
            while(num>0):
                abcd = abcd + num%10
                num = num//10
            num = abcd
            if(len(str(num))==1):
                return(num)
        return(num)
            
        