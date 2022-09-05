class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        abcd = []
        while(num>0):
            abcd.append(num%10)
            num=num//10
        abcd = sorted(abcd)
        print(abcd)
        a = str(abcd[0])+str(abcd[3])
        b = str(abcd[1])+str(abcd[2])
        
        return(int(a)+int(b))