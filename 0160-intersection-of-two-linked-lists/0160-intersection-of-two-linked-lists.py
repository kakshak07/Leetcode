# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        dictP = set()
        pointA = headA
        pointB = headB
        while pointA is not None:
            dictP.add(pointA)
            pointA = pointA.next
        while pointB is not None:
            if pointB in dictP:
                return pointB
            pointB = pointB.next
        
            
            
        