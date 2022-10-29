# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        "1 -> 2 -> 3 -> 4 -> 5"
        "1 -> 5 -> 2 -> 4 -> 3"
        "1 -> 2 -> 3    5 -> 4"
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
            
        
        