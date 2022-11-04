# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], mi = float("inf"), ma = float("-inf")) -> bool:
        if root is None:
            return True
        if root.val >= mi or root.val <=ma:
            return False
        return self.isValidBST(root.left, min(root.val, mi), ma ) and self.isValidBST(root.right,  mi, max(ma, root.val) )