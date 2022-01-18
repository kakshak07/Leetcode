class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        neighbors = {(i, j) for i in range(-1, 2) for j in range(-1, 2)}
        n = len(grid)
        
        if grid[0][0] == 1:
            return -1
        
        q = [(0, 0, 1)] #position i, position j, number of hops
        
        grid[0][0] = 1 #mark starting cell as visited
        
        while q:
            curr_i,curr_j,hops = q.pop(0)

            if curr_i == n-1 and curr_j == n-1:
                return hops

            for i,j in neighbors:
                if 0 <= curr_i+i < n and 0 <= curr_j+j < n: #check that neighbor is in bounds
                    #check that cell is NOT visited
                    if grid[curr_i+i][curr_j+j] == 0:
                        grid[curr_i+i][curr_j+j] = 1 #mark cell as visited
                        q.append((curr_i+i, curr_j+j, hops+1))

        return -1