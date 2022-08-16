# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        list_values = []
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            list_values.append(node)
            dfs(node.right)
        dfs(root)
        # print(list_values)
        t = sorted(n.val for n in list_values)
        for i in range(len(list_values)):
            list_values[i].val = t[i]
        # print(t)
        