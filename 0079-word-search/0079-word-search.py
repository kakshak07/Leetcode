class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i,j,stringWord):
            # print(i,j,stringWord,visited,board[i][j])
            if len(stringWord) == 0:
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] != stringWord[0]:
                return False
            # print(i,j,stringWord,visited,board[i][j])
            if board[i][j] == stringWord[0]:
                # visited.add((i,j))
                temp = board[i][j]
                board[i][j] = "#"
                a = dfs(i+1,j, stringWord[1:])
                b = dfs(i,j+1, stringWord[1:])
                c = dfs(i-1,j, stringWord[1:])
                d = dfs(i,j-1, stringWord[1:])
                board[i][j] = temp
            return a or b or c or d
                
            
            
        # w = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                # visited = []
                print(i,j)
                if dfs(i,j,word):
                    return True
        return False
                
        