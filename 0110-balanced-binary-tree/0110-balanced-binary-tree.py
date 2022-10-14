# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def max_height(root):
            if not root:
                return 0
            return 1+max(max_height(root.left), max_height(root.right))
        # def min_height(root):
        #     if not root:
        #         return 0
        #     return 1+min(min_height(root.left), min_height(root.right))
        def traverse(root):
            if root==None:
                return True
            t = abs(max_height(root.left)- max_height(root.right))
            if t>1:
                return False
            left = traverse(root.left)
            right = traverse(root.right)
            # if not left or not right:
            #     return False
            return left and right
            # return left and right
            
     
        # print(t,t1)
        return traverse(root)
        