class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        str1 = ''
        while columnNumber > 0:
            chr1 = columnNumber % 26
            if chr1 == 0:
                chr1 = 26
                columnNumber -= 1
            str1 = chr(ord('A')+chr1-1) + str1
            columnNumber = columnNumber//26

        return str1