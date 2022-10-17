# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Time = O(m+n)
Space = O(m)
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_set = set()
        while headB is not None:
            node_set.add(headB)
            headB = headB.next
        
        while headA is not None:
            if headA in node_set:
                return headA
            headA = headA.next
        
        return None