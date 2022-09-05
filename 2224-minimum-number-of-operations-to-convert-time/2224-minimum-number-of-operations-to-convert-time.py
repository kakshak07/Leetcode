class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        
        time1 = 60*int(current[0:2])+int(current[3:5])
        time2 = 60*int(correct[0:2])+int(correct[3:5])
        minute = time2-time1
        
        abcd = [1,5,15,60]
        count = 0
        for i in range(len(abcd)-1,-1,-1):
            if(minute//abcd[i]>0):
                count = count + minute//abcd[i]
                minute = minute - abcd[i]*(minute//abcd[i])
        return(count)
        