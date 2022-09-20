class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        
        t1 = [False]*row
        t2 = [False]*col
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    t1[i] = True
                    t2[j] = True
                    
        for i in range(row):
            for j in range(col):
                if(t1[i]==True or t2[j]==True):
                    matrix[i][j]=0
        return(matrix)