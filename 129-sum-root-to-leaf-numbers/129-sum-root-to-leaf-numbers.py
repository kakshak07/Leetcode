# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def traversal(curr, sum_val):
            if not curr:
                return 0
            sum_val = sum_val*10 +curr.val
            
            if not curr.left and not curr.right:
                return(sum_val)
            return(traversal(curr.left, sum_val)+traversal(curr.right, sum_val))
        return(traversal(root, 0))
        