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
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
         
        cur = slow.next
        slow.next = None
        tail = None
        while cur:
            next_node = cur.next
            cur.next = tail
            tail = cur
            cur = next_node
        
        
        dummy = cur = ListNode()
        while tail:
            cur.next = head
            head = head.next
            cur = cur.next
            
            cur.next = tail
            tail = tail.next
            cur = cur.next
            
        cur.next = head
        
        return dummy.next
        