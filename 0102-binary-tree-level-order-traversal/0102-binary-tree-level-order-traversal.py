# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        new_queue = [root]
        list_of_elements = []
        
        while len(new_queue):
            level = []
            for i in range(len(new_queue)):
                t = new_queue.pop(0)
                level.append(t.val)
                if t.left: 
                    new_queue.append(t.left)
                if t.right:
                    new_queue.append(t.right)
            list_of_elements.append(level)
        return(list_of_elements)
        return []
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not root: return []
        
#         queue, result = [root], []
        
#         while len(queue):
#             level = []
#             for i in range(len(queue)):
#                 t = queue.pop(0)
#                 level.append(t.val)
#                 if t.left: queue.append(t.left)
#                 if t.right: queue.append(t.right)
#             result.append(level)
#         return(result)
        