# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        paths = []
        def dfs(string, node):
            string += chr(97+node.val)
            if node.left: dfs(string, node.left)
            if node.right: dfs(string, node.right)
            if not node.right and not node.left: paths.append(string[::-1])
        dfs("", root)
        paths.sort()
        return(paths[0])
        
        
        