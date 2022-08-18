class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.split(' ')
        nums=[int(i) for i in s if i.isdigit()]
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                return False
        return True