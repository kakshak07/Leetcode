class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        counter = 0
        def dfs(isConnected, i):
            for j in range(len(isConnected[i])):
                if(isConnected[i][j] == 1):
                    isConnected[i][j] = 0
                    dfs(isConnected, j)
                    
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if(isConnected[i][j] == 1):
                    counter += 1
                    dfs(isConnected, i)
        return(counter)
            
        