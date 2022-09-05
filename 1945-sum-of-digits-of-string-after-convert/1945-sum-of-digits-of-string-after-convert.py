class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        w= ""
        for i in s:
            w = w+str(ord(i)-96)
        abcd = int(w)
        su=0
        for i in range(k):
            su=0
            while(abcd>0):
                su=su+abcd%10
                abcd = abcd//10
            abcd = su
            print(su)
        return(su)
                
        # while(len(str(num))!=1):
        #     abcd = 0
        #     while(num>0):
        #         abcd = abcd + num%10
        #         num = num//10
        #     num = abcd
        #     if(len(str(num))==1):
        #         return(num)
        # return(num)