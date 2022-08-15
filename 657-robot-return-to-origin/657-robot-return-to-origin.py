class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        
        for i in moves:
            if(i == 'L'):
                x = x + 1
            if(i == 'R'):
                x = x - 1
            if(i == 'U'):
                y = y + 1
            if(i == 'D'):
                y = y - 1
        if(x == 0 and y == 0):
            return(True)
        else:
            return(False)