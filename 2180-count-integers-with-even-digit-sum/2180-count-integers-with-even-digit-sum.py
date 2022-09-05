class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        
    # def countEven(self, num: int) -> int:
        n, dSum = num, 0
        while n > 0: # Calculate digit sum of numbers
            dSum += n%10
            n = n//10
        if num % 2 == 0 and dSum % 2 == 1:
            return num//2 - 1
        return num//2