class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        def check_movies(i, x, y, s):
            count = 0
            new_string = s[i:len(s)]
            # print(new_string,x,y)
            for j in new_string:
                if(j == 'L'):
                    y = y - 1
                if(j == 'R'):
                    y = y + 1
                if(j == 'U'):
                    x = x - 1
                if(j == 'D'):
                    x = x + 1
                # print(x,y)
                if(x < 0 or y < 0 or x>=n or y>=n):
                    # print("hi")
                    list_of_c_m.append(count)
                    return
                    
                else:
                    count = count + 1
            list_of_c_m.append(count)
                    
        
        list_of_c_m = []
        for i in range(len(s)):
            x = startPos[0]
            y = startPos[1]
            check_movies(i, x, y, s)
        return(list_of_c_m)
            
        