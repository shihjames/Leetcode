# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Time = O(n)
Space = O(1)
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        slow.next = None
        rev = None
        while cur:
            nex = cur.next
            cur.next = rev
            rev = cur
            cur = nex
        
        dummy = cur = ListNode()
        while rev:
            cur.next = head
            head = head.next
            cur = cur.next
            cur.next = rev
            cur = cur.next
            rev = rev.next
        cur.next = head
        return dummy.next
            
        
        