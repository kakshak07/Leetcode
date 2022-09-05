class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dict1 = {}
        
        while(True):
            abcd = n
            su1 = 0
            while(abcd>0):
                su1 = su1 + (abcd%10)**2
                abcd = abcd//10
            if(su1 in dict1):
                return False
            dict1[n] = su1
            n = su1
            
            if(su1 == 1):
                return True
            