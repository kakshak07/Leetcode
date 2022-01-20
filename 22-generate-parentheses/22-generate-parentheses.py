class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Result array to store all the possible parenthesis
        parenthesis = []
        def backtrack(string = "", left = 0, right = 0):
            if len(string) == 2 * n:
                parenthesis.append(string)
                return
            if left < n:
                backtrack(string + "(", left+1, right)
            if right < left:
                backtrack(string + ")", left, right+1)
        backtrack()
        return parenthesis