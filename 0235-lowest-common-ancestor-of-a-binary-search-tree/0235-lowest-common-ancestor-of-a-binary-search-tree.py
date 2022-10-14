# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        
        t2 = []
        # t1.append(root.val)
        z = p.val
        def traverse(root, z,t1):
            if not root:
                return
            t1.append(root.val)
            if root.val == z:
                return root
            elif root.val>z:
                traverse(root.left, z,t1)
            else:
                traverse(root.right, z,t1)
            # return
        t1 = []
        traverse(root,p.val, t1)
        traverse(root,q.val, t2)
        t1.reverse()
        t2.reverse()
        for i in t1:
            if i in t2:
                w=i
                break
        print(t1,t2)
        print(w)
        def newtraversal(root,w):
            if root.val==w:
                print("hello")
                return root
            elif root.val>w:
                return newtraversal(root.left,w)
            elif root.val<w:
                return newtraversal(root.right,w)            
        return( newtraversal(root,w))
        # return root
                