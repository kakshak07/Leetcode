class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        k, tot = 5, 0
        while k <= n:
            tot += n // k
            k = k * 5
        return tot